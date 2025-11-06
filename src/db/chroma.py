from functools import lru_cache
from langchain_chroma import Chroma

from functions.embedder import get_embedder


@lru_cache()
def get_chroma_client():
    return Chroma(
        collection_name="my_collection",
        embedding_function=get_embedder(),
        persist_directory="src/db/chroma_db"
    )
