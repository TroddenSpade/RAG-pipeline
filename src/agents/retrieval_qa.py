from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langgraph.types import interrupt

from llm.clients import get_jabir_client
from data_types.types import RetrievalOutputType
from llm.prompts import retrieval_qa_prompt


retrieval_qa_parser = PydanticOutputParser(pydantic_object=RetrievalOutputType)

prompt = PromptTemplate(
    input_variables=["query", "context_text"],
    template=retrieval_qa_prompt,
    partial_variables={
        "format_instructions": retrieval_qa_parser.get_format_instructions()
    },
)

llm = get_jabir_client()
retrieval_qa_chain = prompt | llm.with_structured_output(RetrievalOutputType)


def retrieval_qa(query: str, context_text: str) -> RetrievalOutputType:
    response = retrieval_qa_chain.invoke({
        "query": query,
        "context_text": context_text
    })

    return response
