from fastapi import APIRouter, File, UploadFile

from api.schemas import QueryRequest, QueryResponse
from rag.ingest import ingest_single
from rag.retrieve import retrieve

router = APIRouter()


@router.get("/")
def read_root():
    return "Hello World"



@router.post("/ingest")
async def ingest_file(file: UploadFile = File(...)):
    try:
        file_path = "static/data/" + file.filename

        with open(file_path, "wb") as f:
            f.write(await file.read())
            f.close()
    except Exception as e:
        return {"message": "Error uploading file"}

    ingestion_summary = ingest_single(file_path)

    return {
        "message": "File uploaded successfully",
        "ingestion_summary": ingestion_summary,
    }



@router.post("/query", response_model=QueryResponse)
async def query(req: QueryRequest):
    response = retrieve(req.query, req.k, req.filters)

    return response