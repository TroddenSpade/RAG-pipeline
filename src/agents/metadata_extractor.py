from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langgraph.types import interrupt

from llm.clients import get_jabir_client
from data_types.types import MetaDataType
from llm.prompts import metadata_extractor_prompt


metadata_parser = PydanticOutputParser(pydantic_object=MetaDataType)

prompt = PromptTemplate(
    input_variables=["document"],
    template=metadata_extractor_prompt,
    partial_variables={
        "format_instructions": metadata_parser.get_format_instructions()
    },
)

llm = get_jabir_client()
metadata_extractor_chain = prompt | llm.with_structured_output(MetaDataType)


def metadaata_extractor(doc: str) -> MetaDataType:
    metadata = metadata_extractor_chain.invoke({"document": doc})

    return metadata
