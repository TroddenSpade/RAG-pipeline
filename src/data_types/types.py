from typing import Annotated, Optional
from pydantic import BaseModel, Field

from api.schemas import SourceItem


class MetaDataType(BaseModel):
    """
    metadata of the documents
    """
    id: Optional[str] = Field(
        description="id of the document",
        default=None
    )
    source: Optional[str] = Field(
        description="source of the document",
        default=None
    )
    title: Optional[str] = Field(
        description="title of the document",
        default=None
    )
    date: Optional[str] = Field(
        description="date of the document",
        default=None
    )


class DocumentType(BaseModel):
    """
    metadata of the documents
    """
    text: str = Field(
        description="text of the document"
    )
    file_src: Optional[str] = Field(
        description="file source of the document",
        default=None
    )
    metadata: Optional[MetaDataType] = Field(
        description="metadata of the document",
        default=None
    )

class RetrievalOutputType(BaseModel):
    answer: str
    sources: list[SourceItem]