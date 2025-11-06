from functools import lru_cache
from langchain_openai import ChatOpenAI


@lru_cache()
def get_jabir_client():
    return ChatOpenAI(
        model = "jabir-400b",
        api_key="FAKE",
        base_url="https://openai.jabirproject.org/v1",
        # temperature=0.9,
    )


if __name__ == "__main__":
    client = get_jabir_client()
    print(client.invoke("hello world").content)