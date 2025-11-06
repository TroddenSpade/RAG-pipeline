from pydantic import BaseModel
from typing import Optional, Dict

class QueryRequest(BaseModel):
    query: str
    k: Optional[int] = 5
    filters: Optional[Dict[str, str]] = None


class SourceItem(BaseModel):
    file_src: str
    title: str
    date: str
    id: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]