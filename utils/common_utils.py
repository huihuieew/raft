from typing import List, Any
import json
from openai import BadRequestError, OpenAI
import os
from volcenginesdkarkruntime import Ark



def get_chunkstr(chunks: List[dict]):
    chunkstr = ""
    for idx,chunk in enumerate(chunks):
        chunkstr += f"chunk: {idx}, source: {chunk['source']}\n{chunk['chunk']}"
        chunkstr += "\n"
    return chunkstr

def load_articles(chunks_path):
    with open(chunks_path, "r", encoding="utf-8") as f:
        articles = json.load(f)
        return articles

def build_openai_client_chat(env_prefix : str = "COMPLETION", **kwargs: Any) -> OpenAI:
    """
    Build OpenAI client based on the environment variables.
    """

    client = OpenAI(
        api_key=os.getenv("COMPLETION_OPENAI_API_KEY"),
        base_url=os.getenv("COMPLETION_OPENAI_BASE_URL")
    )

    return client.chat.completions.create

def build_doubao_embedding(env_prefix : str = "COMPLETION", **kwargs: Any) -> Ark:
    """
    Build OpenAI client based on the environment variables.
    """

    emb_client = Ark(
        api_key=os.getenv("COMPLETION_OPENAI_API_KEY"),
    )

    return emb_client.embeddings.create