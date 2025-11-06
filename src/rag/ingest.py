import os
import time
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader

from agents.metadata_extractor import metadaata_extractor
from config.parameters import DOCUMENT_HEAD_CHAR_LIMIT
# from functions.file_loader import load_document
from data_types.types import DocumentType
from db.chroma import get_chroma_client
from functions.splitter import get_text_splitter


def add_documents_db(documents: list[DocumentType]) -> None:
    db = get_chroma_client()

    for idx, doc in enumerate(documents):
        llm_metadata = metadaata_extractor(doc.page_content[:DOCUMENT_HEAD_CHAR_LIMIT])
        doc.metadata.update({
            "file_src": doc.metadata["source"],
            "title": llm_metadata.title,
            "date": llm_metadata.date,
            "source": llm_metadata.source,
            "id": str(time.time()) + "-" + str(idx),
        })

    chunks = get_text_splitter().split_documents(documents)
    db.add_documents(chunks)

    return {
        "chunk_len": len(chunks),
        "token_len": sum([len(doc.page_content) for doc in documents]),
    }


def ingest_single(file_src: str) -> None:
    try:
        loader = UnstructuredFileLoader(file_src)
        document = loader.load()
    except Exception as e:
        print(f"ERROR: {e}")
        return None

    ingestion_summary = add_documents_db(document)

    return ingestion_summary


def ingest_all(data_dir: str) -> None:
    loader = DirectoryLoader(data_dir)
    documents = loader.load()
    add_documents_db(documents)
    