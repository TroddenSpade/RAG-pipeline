import os
from fastapi import FastAPI
import uvicorn

from api.routes import router
from rag.ingest import ingest_all


app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    db_exists = os.path.exists("src/db/chroma_db") and len(os.listdir("src/db/chroma_db/")) > 0

    if db_exists:
        print("Loading existing Chroma database...")
    else:
        print("Ingesting all documents...")
        ingest_all(os.path.join(os.getcwd(), "static"))

    uvicorn.run(app, host="127.0.0.1", port=8000)
