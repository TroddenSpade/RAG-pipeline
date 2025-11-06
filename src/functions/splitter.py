from functools import lru_cache
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.parameters import CHUNK_OVERLAP, CHUNK_SIZE


@lru_cache()
def get_text_splitter():
    return RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    