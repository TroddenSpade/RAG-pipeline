from agents.retrieval_qa import retrieval_qa
from db.chroma import get_chroma_client


def retrieve(query: str, k: int = 5, filters: dict[str, str] = None):
    results = get_chroma_client().similarity_search(
        query,
        k=k,
        filter=filters
    )
    context_text = "\n\n---\n\n".join([doc.page_content for doc in results])
    res = retrieval_qa(query, context_text)

    return {
        "answer": res.answer,
        "sources": [doc.page_content for doc in results]
    }
