import os
from PyPDF2 import PdfReader

def _load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def _load_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def load_document(data_dir: str = "static"):
    if data_dir.endswith(".txt"):
        return (data_dir, _load_txt(data_dir))

    elif data_dir.endswith(".pdf"):
        return (data_dir, _load_pdf(data_dir))

    return (data_dir, None)
