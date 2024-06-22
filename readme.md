# RAG Based Q&A APP
This is a demo RAG-based application, currently, I am using faiss vector store.

It can be replaced with a vector database/index like Opensearch,milvus


# Tech Stack
1. Langchain
2. azure openai
3. RAG


# How to run
1. add azure openai gpt4-0 key and endpoint in .env file
2. run app.py if you want to run as api endpoint.
3. if you want to run UI of this application
```shell
    streamlit run main.py
```



# How to index document to vector db
1. Add files to documents folder
2. run python script
```shell
document_processor/document_processor.py
```

