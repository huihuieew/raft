from typing import List, Any
from openai import BadRequestError, OpenAI
import os 
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_chunkstr(chunks: List[dict]):
    chunkstr = ""
    for idx,chunk in enumerate(chunks):
        chunkstr += f"chunk: {idx}, source: {chunk['source']}\n{chunk['chunk']}"
        chunkstr += "\n"
    return chunkstr

build_qa_messages = {
    "gpt": lambda chunk, x : [
            {"role": "system", "content": """You are a synthetic question-answer pair generator. Given a chunk of context about 
             some topic(s), generate %s example questions a user could ask and would be answered using information from the chunk. 
             For example, if the given context was a Wikipedia paragraph about the United States, an example question could be 
             'How many states are in the United States?'""" % (x)},
            {"role": "system", "content": "The questions should be able to be answered in a few words or less. Include only the questions in your response."},
            {"role": "user", "content": str(chunk)}
        ],
    "llama": lambda chunk, x : [
            {"role": "system", "content": 
                """You are a synthetic question generator.
                
                Instructions:
                - Given a chunk of context about some topic(s), generate %s example questions a user could ask
                - Questions should be answerable using only information from the chunk.
                - Generate one question per line
                - Generate only questions
                - Questions should be succinct

                Here are some samples:
                Context: A Wikipedia paragraph about the United States, 
                Question: How many states are in the United States?

                Context: A Wikipedia paragraph about vampire bats, 
                Question: What are the different species of vampire bats?
                """ % (x)},
            {"role": "system", "content": "The questions should be able to be answered in a few words or less. Include only the questions in your response."},
            {"role": "user", "content": str(chunk)}
        ],
    "deepseek": lambda chunk, x : [
            {"role": "system", "content": f"你是一个合成问答对的生成器。给定一个关于某些话题的上下文，生成{x}个用户可能会问到的示例问题，并且使用该上下文进行回答。例如，如果给定的上下文是维基百科中关于美国的段落，则示例问题可以是“美国的州有多少？”。"},
            {"role": "system", "content": "用中文进行提问，并且这些问题应该用简洁的语言回答。在回复中只包含问题。"},
            {"role": "user", "content": str(chunk)}
        ],
    "deepseek-v2": lambda academic_paper, x : [
            {"role": "system", "content": "你是一个乐于助人的半导体显示技术领域的专家。"}, 
            {"role": "user", "content": f"""你是一位半导体显示技术领域的资深专家，擅长从技术文献中提炼核心知识点。你的职责是从论文中生成问题和相应的答案，问题和相应的答案对需要提供给资深的人员学习，问题和相应的答案的质量要高。请根据输入的学术论文内容，生成{x}个需要逻辑推理才能解答的高质量技术问题，请确保这些问题能够直接从论文中找到答案。这些问题将用于资深研究人员的专业能力评估，需满足以下要求：
【核心要求】
问题设计准则：
a) 首先你需要阅读全文，并判断哪些文本中涉及到逻辑推理的内容。然后你需要根据逻辑推理的内容设计相应的问题。
b) 问题必须基于论文中的技术原理进行设计，问题的描述必须明确清晰全面，问题中主语或名词的描述必须要精准、全面且具备通用性，专有名词应该让行业人员都能看懂。
c) 问题中请不要引用文献或者文章定义的专有名词，请结合你自身半导体的显示领域的知识和文章内容，生成普适通用的问题，在不阅读论文的情况也能正常理解问题所表达的含义。
d) 问题中的名词描述不可以缩写，需要与论文中的描述一致。例如论文中提到的是“OLED材料”，问题中不能简化为“材料”。例如论文中提到的是“LTPS器件”，问题中不能简化为“器件”。
e) 不要针对于论文中的某个特定示例进行提问，问题尽量使顶尖科学家在不阅读论文的情况下也能理解和回答。且问题不能包含“书本”、“论文”、“本文”、“本实验”、“报道”、“xx等人的研究”等相关信息； 

科学严谨性：
a) 因果链：问题需呈现完整技术逻辑链（如：机制A如何影响参数B，进而导致现象C）
b) 周密性：过程需要科学严谨，逐步思考，确保问题和对应的答案来源于论文的内容。且答案需要能在论文中完全找到详细的描述。
问题简洁：问题要凝练简洁。

【禁止事项】
× 禁止使用"本文/本研究/本实验"等论文自指表述
× 禁止提问孤立概念（如：XX技术的定义是什么）
× 禁止超出论文技术范围的假设性问题

【格式要求】：用中文输出。当前阶段只设计问题，不输出答案。严格按照以下格式输出你设计的问题：
[[1]] 第1个问题
[[2]] 第2个问题
[[3]] 第3个问题 

[学术论文的开始]
{academic_paper}
[学术论文的结束]"""
            },
        ]
}

def generate_instructions_gen(chat_completer: Any, chunk: Any, x: int = 2, model: str = None, prompt_key : str = "deepseek-v2") -> list[str]:
    """
    Generates `x` questions / use cases for `chunk`. Used when the input document is of general types 
    `pdf`, `json`, or `txt`.
    """
    try:
        # 判断 chunk 是否是 list
        if isinstance(chunk, list):
            chunk2str = get_chunkstr(chunk)
            chunk = chunk2str
        response = chat_completer(
            model=model,
            messages=build_qa_messages[prompt_key](chunk, x),
            max_tokens=min(100 * x, 512), # 25 tokens per question
        )
    except BadRequestError as e:
        if e.code == "content_filter":
            # logger.warning(f"Got content filter error, skipping chunk: {e.message}")
            return []
        raise e

    content = response.choices[0].message.content
    queries = content.split('\n') if content else []
    queries = [q for q in queries if any(c.isalpha() for c in q)]

    return queries


def get_chunk4(i, chunks):
    # 取 i 和 i+4 个chunk
    if (i+4) >= len(chunks):
        chunk4 = chunks[i:]
    else:
        chunk4 = chunks[i: i+4] 
    return chunk4
def build_openai_client_chat(env_prefix : str = "COMPLETION", **kwargs: Any) -> OpenAI:
    """
    Build OpenAI client based on the environment variables.
    """

    client = OpenAI(
        api_key=os.getenv("COMPLETION_OPENAI_API_KEY"),
        base_url=os.getenv("COMPLETION_OPENAI_BASE_URL")
    )

    return client.chat.completions.create

    
