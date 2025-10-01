# # rag_pipeline.py
# import os
# import glob
# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.schema import Document
# from dotenv import load_dotenv

# load_dotenv()


# def build_rag():
#     print("📚 Loading local docs...")
#     doc_files = glob.glob("docs/*.txt")
#     docs = []
#     for file in doc_files:
#         with open(file, "r", encoding="utf-8") as f:
#             content = f.read()
#             docs.append(Document(page_content=content,
#                         metadata={"source": file}))

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500, chunk_overlap=100)
#     split_docs = splitter.split_documents(docs)

#     embedder = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2")
#     vectorstore = FAISS.from_documents(split_docs, embedder)

#     print("✅ RAG ready with", len(split_docs), "chunks")
#     return vectorstore.as_retriever(search_kwargs={"k": 3})


# retriever = build_rag()


# def query_rag(question: str):
#     docs = retriever.get_relevant_documents(question)
#     if not docs:
#         return None
#     context = "\n".join([d.page_content for d in docs])
#     return f"Based on my local knowledge:\n{context}"


# with logging

import os
import glob
import logging
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)


def build_rag():
    logger.info("📚 Loading local docs...")
    doc_files = glob.glob("docs/*.txt")
    docs = []
    for file in doc_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            docs.append(Document(page_content=content,
                        metadata={"source": file}))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100
    )
    split_docs = splitter.split_documents(docs)

    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(split_docs, embedder)

    logger.info(f"✅ RAG ready with {len(split_docs)} chunks")
    return vectorstore.as_retriever(search_kwargs={"k": 3})


retriever = build_rag()


def query_rag(question: str):
    docs = retriever.get_relevant_documents(question)
    if not docs:
        logger.warning("No relevant documents found for the query.")
        return None
    context = "\n".join([d.page_content for d in docs])
    logger.info(f"Retrieved {len(docs)} documents for the query.")
    return f"Based on my local knowledge:\n{context}"
