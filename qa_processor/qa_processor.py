from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_openai.chat_models import AzureChatOpenAI
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import os
from config import Config
from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub


class QAProcessor:
    def __init__(self):
        self.config = Config("config/config.yaml")
        self.api_key = os.getenv("AZURE_OPENAI_VISION_KEY")
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.vector_db_path = self.config.get("vector_db_path")

        # Load the FAISS index
        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.config.get("embedding_model")
        )

        # Initialize the FAISS vector store
        self.vector_store = FAISS.load_local(
            self.vector_db_path,
            self.embeddings,
            index_name=self.config.get("index_name"),
            allow_dangerous_deserialization=True,
        )

        # Initialize the LLM
        self.llm = AzureChatOpenAI(
            temperature=0.1,
            model_name="gpt-4o",
            deployment_name="gpt4o",
            azure_endpoint=self.endpoint,
            openai_api_key=self.api_key

        )
        # Initialize the QA chain
        retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
        combine_docs_chain = create_stuff_documents_chain(
            self.llm, retrieval_qa_chat_prompt
        )
        # Initialize the RAG chain
        self.rag_chain = create_retrieval_chain(
            self.vector_store.as_retriever(), combine_docs_chain
        )

    def ask_question(self, question) -> dict:
        # Use the RAG chain to get the answer
        result = self.rag_chain.invoke({"input": question})
        return result


if __name__ == "__main__":
    load_dotenv()
    qa_processor = QAProcessor()
    answer = qa_processor.ask_question(
        question="What precautions needs to be taken in terms of clothing and hair?"
    )
    print(answer['answer'])
