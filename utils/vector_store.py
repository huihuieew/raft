# 离线流程 
# 向量库存储

from utils.common_utils import load_articles, build_doubao_embedding
import json
import os
import uuid
from llama_index.core.schema import TextNode

emb_model = build_doubao_embedding()
def get_chunk_with_embedding(chunks_path, embedding_path):
    article_chunks = load_articles(chunks_path)
    for a_name, chunks in article_chunks.items():
        print(f"Processing {a_name}")
        chunk_texts = [chunk["chunk"] for chunk in chunks]
        response = emb_model(
            # model="doubao-embedding-large-text-250515",
            model="doubao-embedding-text-240715",
            input=chunk_texts,
            encoding_format="float"
        ) 
        chunks_with_embedding = []
        for chunk, data in zip(chunks, response.data):
            chunk["embedding"] = data.embedding
            chunk["doc_id"] = str(uuid.uuid4())
            chunks_with_embedding.append(chunk)
        save_embeddings(chunks_with_embedding, embedding_path)
    return chunks_with_embedding
def save_embeddings(chunks_with_embedding, output_path):
    # 判断 filename 是否存在，如果存在则追加写入，否则创建新文件
    if os.path.exists(output_path):
        with open(output_path, 'r', encoding="utf-8") as f:
            existing = json.load(f)
        existing.extend(chunks_with_embedding)
        with open(output_path, 'w', encoding="utf-8") as f:
            json_str = json.dumps(existing, ensure_ascii=False, indent=4)
            json_str = json_str.replace(',\n\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020', ', ')
            f.write(json_str)
            # json.dump(existing, f, ensure_ascii=False, indent=4)
    else:
        with open(output_path, 'w', encoding="utf-8") as f:
            json_str = json.dumps(chunks_with_embedding, ensure_ascii=False, indent=4)
            # 替换掉 list 中的换行符，让 list 内容显示在一行
            json_str = json_str.replace(',\n\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020', ', ')
            f.write(json_str)
    print(f"Embedding saved to {output_path}")

def get_nodes(embedding_path):
    chunks_with_embedding = load_articles(embedding_path)
    chunks = chunks_with_embedding
    nodes = []
    for chunk in chunks:
        node = TextNode(
            text=chunk["chunk"], 
            id=chunk["chunk_id"], 
            doc_id=chunk["doc_id"],
            embedding=chunk["embedding"],
            metadata={
                "source": chunk["source"],
            }
        )
        nodes.append(node)
    return nodes


import os
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core.storage.docstore import SimpleDocumentStore

def storage_embedding_nodes(
        embedding_path,
        docstore_path="llama_index/docstore.json",
        chroma_db="llama_index/chroma_db",
        chroma_name="sc_collection01",
        storage_dir="./vector_index01",
    ):
    allnodes = get_nodes(embedding_path)
    docstore = SimpleDocumentStore()
    docstore.add_documents(allnodes)
    
    db = chromadb.PersistentClient(path=chroma_db)
    chroma_collection = db.get_or_create_collection(name=chroma_name)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(
        vector_store=vector_store, 
        docstore=docstore
    )
    vector_store.add(allnodes)
    docstore.persist(persist_dir=docstore_path)
    storage_context.persist(persist_dir=storage_dir)


