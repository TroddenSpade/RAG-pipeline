from langchain_core.embeddings import Embeddings
import torch
from sentence_transformers import SentenceTransformer
from langchain_ollama import OllamaEmbeddings
from functools import lru_cache


class Embedder(Embeddings):
    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
        device: str = None
    ):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        try:
            self.model = SentenceTransformer(model_name, device=self.device)
        except Exception as e:
            print(f"ERROR loading model '{model_name}': {e}")
            raise e
        
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed search docs.

        Args:
            texts: List of text to embed.

        Returns:
            List of embeddings.
        """
        return self.model.encode(texts)

    def embed_query(self, text: str) -> list[float]:
        """Embed query text.

        Args:
            text: Text to embed.

        Returns:
            Embedding.
        """
        return self.model.encode(text)



@lru_cache()
def get_embedder(
    # heydariAI/persian-embeddings
    model_name: str = "heydariAI/persian-embeddings", 
    device: str = None
) -> Embedder:
    """
    a single global instance of the embedder.
    """
    return Embedder(model_name, device)

