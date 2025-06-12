# from common_utils import *
from utils.common_utils import *
from concurrent.futures import ThreadPoolExecutor, as_completed
import os 
import json
from tqdm import tqdm

prompt_templates = {
    "deepseek": """
        Question: {question}\nContext: {context}\n
        使用上述给定的上下文，回答问题。注意：
        - 首先，请提供有关如何回答问题的详细 reasoning。
        - 在 reasoning 中，如果需要复制上下文中的某些句子，请将其包含在 ##begin_quote## 和 ##end_quote## 中。 这意味着 ##begin_quote## 和 ##end_quote## 之外的内容不是直接从上下文中复制的。
        - 结束你的回答，以 final answer 的形式 <ANSWER>: $answer，答案应该简洁。
        你必须以<Reasoning>: 开头，包含 reasoning 相关的内容；以 <ANSWER>: 开头，包含答案。
    """,
    "deepseek-v1": """{
        "instruction":"你是一个半导体显示领域的资深专家，你掌握TFT、OLED、LCD、QLED、EE、Design等显示半导体显示领域内的相关知识。请根据输入中的切片信息和问题进行回答。切片信息是可能相关的资料，切片信息的内容庞杂，不一定会包含目标答案，请仔细阅读每个切片后再作答，不得出现错误。",
        "input": {
            "context": "{context}",
            "question": "{question}"
        },
        "output": {
            "answer": "根据切片中提供的有效信息对问题进行详尽的回答，推荐分点回答格式。"
        },
        "requirements": {
            "criteria": "根据提供的切片信息提取有效信息进行回答",
            "format": "输出内容必须用中文作答。",
            "reasoning" : "在系统内部的think推理过程中，请将参考用到的上下文内容包含在 ##begin_quote## 和 ##end_quote## 中。 "
        }
    }""",
    "deepseek-v2": """{
        "instruction":"你是一个半导体显示领域的资深专家，你掌握TFT、OLED、LCD、QLED、EE、Design等显示半导体显示领域内的相关知识。请根据输入中的切片信息和问题进行回答。切片信息是可能相关的资料，切片信息的内容庞杂，不一定会包含目标答案，请仔细阅读每个切片后再作答，不得出现错误。",
        "input": {
            "context": "{context}",
            "question": "{question}"
        },
        "output": {
            "answer": "根据切片中提供的有效信息对问题进行详尽的回答，推荐分点回答格式。"
        },
        "requirements": {
            "criteria": "根据提供的切片信息提取有效信息进行回答",
            "format": "输出内容必须用中文作答。"
        }
    }"""
}
def gen_answer_prompt(question: str, chunk4: list[dict]) -> list[str]:
    """
    Encode multiple prompt instructions into a single string for the general case (`pdf`, `json`, or `txt`).
    """
    
    messages = []
    chunkstr = get_chunkstr(chunk4)
    prompt = prompt_templates[os.getenv("PROMPT_KEY")].replace("{question}", question).replace("{context}", chunkstr)
    messages.append({"role": "system", "content": "你是一个十分有帮助的RAG问题回答者，你可以根据问题和相关上下文提供答案。"})
    messages.append({"role": "user", "content": prompt})
    return messages

def generate_label(chat_completer: Any, question_dict: dict) -> str | None:
    """
    Generates the label / answer to `question` using `context` and deepseek.
    """
    chunk4 = question_dict["oracle_chunks"]
    question = question_dict["question"]
    messages = gen_answer_prompt(question, chunk4)
    response = chat_completer(
        model=os.getenv("GENERATION_MODEL"),
        messages=messages,
        n=1,
        temperature=0,
        max_tokens=2048,
    )
    reasoning_content = response.choices[0].message.reasoning_content
    response = response.choices[0].message.content
    return response, reasoning_content, question_dict
                
def save_answers(response, reasoning_content, question_dict, article_name, answers_path):
    question_dict["reasoning_answer"] = f"<think>{reasoning_content}\n</think>\n\n{response}"
    # 判断 filename 是否存在，如果存在则追加写入，否则创建新文件
    if os.path.exists(answers_path):
        with open(answers_path, 'r', encoding="utf-8") as f:
            existing_questions = json.load(f)
        # 检查 article_name 是否已经存在于 questions 中
        if article_name in existing_questions:
            existing_questions[article_name].append(question_dict)
        else:
            existing_questions[article_name] = [question_dict]
        with open(answers_path, 'w', encoding="utf-8") as f:
            json.dump(existing_questions, f, ensure_ascii=False, indent=4)
    else:
        with open(answers_path, 'w', encoding="utf-8") as f:
            json.dump({article_name: [question_dict]}, f, ensure_ascii=False, indent=4)
    print(f"Answers saved to {answers_path}")

def gen_answer(questions_path, chat_model, answers_path):
    if os.path.exists(answers_path):
        # articles_answers = load_articles(answers_path)
        print(f"{answers_path} exists. Skipping...")
        return 
    articles_questions = load_articles(questions_path)
    for a_name,question_dicts in articles_questions.items():
        futures = []
        num_questions = len(question_dicts)
        with tqdm(total=num_questions, desc="Answering", unit="file") as pbar:
            with ThreadPoolExecutor(max_workers=2) as executor:
                for question_dict in question_dicts:
                    futures.append(executor.submit(generate_label, chat_model, question_dict))
                for future in as_completed(futures):
                    response, reasoning_content, question_dict = future.result()
                    pbar.update(1)
                    save_answers(response, reasoning_content, question_dict, a_name, answers_path)
                print(f"done {a_name} answers.")
