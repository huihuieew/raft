import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from pathlib import Path
from typing import Literal, Any, get_args, List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from math import ceil
import json
from datasets import Dataset
import pyarrow as pa


DocType = Literal["txt", "md"]
# 2.1 要读取文件的文件名
def read_file_names(data_dir, ext=".md"):
    """\n"""
    file_names = []
    for filename in os.listdir(data_dir):
        file_names.append(filename)
    # 过滤掉 ~$ 开头的文件
    file_names = [file_name for file_name in file_names if not file_name.startswith("~$")]
    file_names = [file_name for file_name in file_names if file_name.endswith(ext)]
    print(f"len(file_names): {len(file_names)}")
    return file_names

def get_chunks(
    data_path: Path, 
    doctype: DocType = "txt", 
    chunk_size: int = 512, 
) -> list[str]:
    """
    Takes in a `data_path` and `doctype`, retrieves the document, breaks it down into chunks of size
    `chunk_size`, and returns the chunks.
    """
    # logger.info(f"Retrieving chunks from {data_path} of type {doctype} using the {model} model.")

    chunks = []
    file_paths = [data_path]
    if data_path.is_dir():
        file_paths = list(data_path.rglob('**/*.' + doctype))

    futures = []
    with tqdm(total=len(file_paths), desc="Chunking", unit="file") as pbar:
        with ThreadPoolExecutor(max_workers=2) as executor:
            for file_path in file_paths:
                futures.append(executor.submit(get_doc_chunks, file_path, doctype, chunk_size))
            for future in as_completed(futures):
                doc_chunks = future.result()
                chunks.extend(doc_chunks)
                pbar.set_postfix({'chunks': len(chunks)})
                pbar.update(1)

    filename = os.path.basename(data_path)
    return chunks, filename

def get_doc_chunks(
    file_path: Path, 
    doctype: DocType = "txt", 
    chunk_size: int = 512,
 ) -> list[str]:
    if doctype == "json":
        with open(file_path, 'r', encoding="utf-8") as f:
            data = json.load(f)
        text = data["text"]
    elif doctype == "txt":
        with open(file_path, 'r', encoding="utf-8") as file:
            data = file.read()
        text = str(data)
    elif doctype == "md":
        with open(file_path, 'r', encoding="utf-8") as file:
            data = file.read()
        text = str(data)
    else:
        raise TypeError("Document is not one of the accepted types: api, pdf, json, txt")
    
    # num_chunks = ceil(len(text) / chunk_size)
    # logger.debug(f"Splitting text into {num_chunks} chunks.")

    # text_splitter = SemanticChunker(embeddings, number_of_chunks=num_chunks)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=0)
    chunks = text_splitter.create_documents([text])
    chunks = [chunk.page_content for chunk in chunks]
    return chunks

def build_or_load_chunks(
        datapath: Path, 
        doctype: str,
        CHUNK_SIZE: int
    ):
    """
    Builds chunks and checkpoints them if asked
    """
    # chunks_ds: Dataset = None
    chunks = None
    # checkpoints_chunks_path = checkpoints_dir / "chunks"
    # logger.info(f"Using checkpoint chunks {checkpoints_chunks_path}")
    # if checkpoints_chunks_path.exists():
    #     chunks_ds = Dataset.load_from_disk(checkpoints_chunks_path)
    #     chunks = chunks_ds
    #     chunks_list = chunks

    if not chunks:
        chunks, filename = get_chunks(datapath, doctype, CHUNK_SIZE)
        chunks_dict = [
            {"chunk": chunk, "source": filename, "chunk_id": idx}
            for idx, chunk in enumerate(chunks)
        ]
        
    # if not chunks_ds:
    #     chunks_table = pa.table({ "chunk": chunks, "source": [filename] * len(chunks), "chunk_id": range(len(chunks)) })
        # chunks_ds = Dataset(chunks_table)
        # chunks_ds.save_to_disk(checkpoints_chunks_path)
    return chunks_dict, filename

def save_chunks(chunks, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(chunks, f, indent=4, ensure_ascii=False)
    print(f"Chunks saved to {filename}")
def get_article_chunks(data_dir, chunks_path):
    filenames = read_file_names(data_dir, ext=".md")
    filenames = filenames[:5]
    articles = []
    count = 0
    for idx,filename in enumerate(filenames):
        data_path = os.path.join(data_dir, filename)
        data_path = Path(data_path)
        chunks_dict, filename = build_or_load_chunks(data_path, "md", 512)
        article = {
            "doc_id": idx,
            "filename": filename,
            "chunks": chunks_dict
        }
        articles.append(article)
        count += len(chunks_dict)
    print(f"len(chunks_all) = {count}")
    save_chunks(articles, chunks_path)
    return articles