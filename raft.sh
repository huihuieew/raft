python3 raft.py \
  --datapath data/RAFT.pdf \
  --output outputs \
  --output-format hf \ # or completion or chat
  --distractors 3 \
  --p 1.0 \
  --doctype pdf \
  --chunk_size 512 \
  --questions 2 \
  --embedding_model text-embedding-v2 \
  --completion_model qwen-plus \
  --openai_key sk-f48122216ef34a308d4da05e4fa4c89a

python raft.py --datapath data/RAFT.pdf --output outputs --output-format hf --distractors 3 --p 1.0 --doctype pdf --chunk_size 512 --questions 2 --completion_model qwen-plus --openai_key sk-f48122216ef34a308d4da05e4fa4c89a
python raft.py --datapath data/97平板显示综述_朱昌昌_llm_correct.md --output outputs_test --output-format hf --distractors 3 --p 1.0 --doctype txt --chunk_size 512 --questions 2 --completion_model qwen-plus --openai_key sk-f48122216ef34a308d4da05e4fa4c89a
