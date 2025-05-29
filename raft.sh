python3 raft.py \
  --datapath data/RAFT.pdf \
  --output outputs \
  --output-format hf \ # or completion or chat
  --distractors 3 \
  --p 1.0 \
  --doctype pdf \
  --chunk_size 512 \
  --questions 2 \
  --system-prompt-key llama \
  --embedding_model doubao-embedding-large-text-250515 \
  --completion_model deepseek-r1-250120 \

# --embedding_model text-embedding-v2 \
# --completion_model qwen-plus \
# --openai_key f40416fd-bfd1-4370-b74f-15c3338d0c58
# --openai_key sk-f48122216ef34a308d4da05e4fa4c89a  ali apikey

python raft.py --datapath data/RAFT.pdf --output outputs --output-format hf --distractors 3 --p 1.0 --doctype pdf --chunk_size 512 --questions 2 --completion_model qwen-plus --openai_key sk-f48122216ef34a308d4da05e4fa4c89a
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test --output-format hf --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model qwen-plus --openai_key sk-f48122216ef34a308d4da05e4fa4c89a
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test01 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test02 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model deepseek-r1-250120 --system-prompt-key llama
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test03 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test04 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test05 --output-format completion --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test06 --output-format completion --distractors 4 --p 1.0 --doctype txt --chunk_size 512 --questions 5 --completion_model deepseek-r1-250120 --system-prompt-key deepseek
