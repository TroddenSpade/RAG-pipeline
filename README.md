# 🧠 RAG Pipeline with ChromaDB, FastAPI & LLM Agents

This project implements a complete **Retrieval-Augmented Generation (RAG)** backend using:

* **FastAPI** — API server for ingestion, querying, and LLM responses
* **ChromaDB** — vector store for embeddings + metadata
* **Custom LLM Agents** — metadata extraction & retrieval QA
* **PDF/Text ingestion pipeline** — chunking, embedding, and metadata generation

It is designed to be **modular, production-ready, and optimized for Persian/Farsi documents**.

---

# Why ChromaDB?

### 🔹 1. High Performance in Similarity Search & Ingestion

* Uses **HNSW**, one of the fastest ANN algorithms
* Millisecond-level similarity queries
* Efficient ingestion & indexing, even locally
* Fully supports **Persian/Farsi embeddings**

### 🔹 2. Scalable & Easy to Deploy

Chroma supports:

* Local embedded mode
* Persistent on-disk mode
* Server mode for distributed or cloud setups

This allows you to:

* Start small
* Scale to Docker/Kubernetes
* Migrate to Milvus/Weaviate later if needed

### 🔹 3. Excellent Tooling & Community Support

* First-class integration with **LangChain**
* Active community + stable development
* Simple debugging thanks to SQLite storage
* Works well with FastAPI, LlamaIndex, HuggingFace, etc.

---

# 📁 Project Structure

```
src/
├── agents/               # LLM-powered agents (retrieval QA + metadata extractor)
├── api/                  # FastAPI routes + schemas
├── config/               # Project-wide configuration
├── data_types/           # Pydantic models and custom types
├── db/                   # ChromaDB wrapper + persisted database
├── functions/            # Embedding, file loading, and chunk splitting
├── llm/                  # LLM clients + prompt templates
├── rag/                  # Ingestion and retrieval pipelines
└── main.py               # FastAPI entrypoint

static/data/              # Example TXT/PDF documents
```

Each folder has a clear responsibility, making the system maintainable and extensible.

---

# 🚀 Features

## ✅ 1. Full RAG Pipeline

Automatically:

* Loads text and PDF files
* Splits into semantic chunks
* Generates embeddings
* Extracts structured metadata
* Saves everything into ChromaDB

## ✅ 2. Retrieval QA Agent

`retrieval_qa.py`:

* Retrieves top-K relevant chunks
* Builds a RAG-optimized prompt
* Uses an LLM to answer accurately
* Returns **answer + sources + similarity scores**

## ✅ 3. Metadata Extraction Agent

Each chunk is enriched with:

* Document ID
* Source filepath
* Title
* Date

### Why This Schema Improves RAG Quality

**Better filtering**
→ query only relevant documents or time ranges

**Faster retrieval**
→ smaller chunks = faster indexing + better similarity search

**Higher accuracy / fewer hallucinations**
→ LLM sees only the correct, context-aligned chunk content

This results in **better grounding and higher answer quality**.

## ✅ 4. FastAPI Backend

### Endpoints

#### **`POST /ingest`**

Upload TXT/PDF → extract → chunk → embed → store

#### **`POST /query`**

Send a question → retrieve chunks → LLM answer

### Example Request

```json
{
  "query": "دخانیات برای چه سنی ممنوع است؟",
  "k": 5
}
```

### Example Response

```json
{
  "answer": "خرید، فروش و مصرف هرگونه محصول دخانیات برای افرادی که در تاریخ یکم ژانویه ۲۰۰۷ و پس از آن به دنیا آمده‌اند، غیرقانونی است.",
  "sources": [
    "«خرید، فروش و مصرف هرگونه محصول دخانیات ...",
    "رویکرد جهانی ممنوعیت نسلی دخانیات ...",
    "به‌گزارش آی‌اف‌ال‌ساینس ...",
    "مالدیو با قانون ممنوعیت نسل‌محور ...",
    "تاریخ‌سازی مالدیو در مبارزه با دخانیات ..."
  ]
}
```

---

# 🔍 How the RAG System Works

## **1️⃣ Ingestion Pipeline**

* Upload file
* Extract text
* Split into chunks
* Compute embeddings
* Extract metadata
* Persist into ChromaDB

## **2️⃣ Query Pipeline**

* Embed query
* Retrieve top-k chunks
* Build RAG prompt
* LLM generates grounded answer
* Return answer + metadata sources

---

# 🔧 Setup

## 1. Clone the repo

```bash
git clone <repo-url>
cd <project-folder>
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Run the API

```bash
python src/main.py
```

Open Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

# 📦 Example Documents

The `static/data/` directory contains Persian TXT & PDF files used to test ingestion.

---
