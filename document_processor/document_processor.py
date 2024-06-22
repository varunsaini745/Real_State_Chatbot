from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import faiss
import numpy as np
from config import Config
import os
from typing import List


class DocumentProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.config = Config(config_path="config/config.yaml")
        self.chunk_size = self.config.get("chunk_size")
        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.config.get("embedding_model")
        )
        self.vector_db = None
        self.index = None

    def load_documents(self) -> List[Document]:
        documents = []
        print("loading documents...")
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                path = os.path.join(self.folder_path, filename)
                reader = TextLoader(path)
                documents.extend(reader.load())
        return documents

    def chunk_and_store(self) -> None:
        documents = self.load_documents()
        print("Extracting documents...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size, chunk_overlap=100
        )
        documents = text_splitter.split_documents(documents)
        print(documents)
        self.index = FAISS.from_documents(documents, self.embeddings)
        print("Saving documents vectors...")
        self.index.save_local(
            folder_path=self.config.get("vector_db_path"),
            index_name=self.config.get("index_name"),
        )
        print("saved all documents to vector db...")


if __name__ == "__main__":
    load_dotenv(".env")
    processor = DocumentProcessor("documents")
    processor.chunk_and_store()
