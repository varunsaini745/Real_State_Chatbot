# RAG Based Q&A APP
This is a demo RAG based application, currently i am using faiss vector store.

It can be replaced with vector database/index like opensearch,milvus


# Tech Stack
1. Langchain
2. azure openai
3. RAG


# How to run
1. add azure openai gpt4-0 key and endpoint in .env file
2. run main.py
```shell
    python main.py
```
3. It will go through provided sample questions and give the answer based on data


# How to index document to vector db
1. Add files to documents folder
2. run python script
```shell
document_processor/document_processor.py
```


# Answers of provided sample question for quick look
Q:What precautions needs to be taken in terms of clothing and hair?

Ans:In terms of clothing and hair, the following precautions need to be taken:

1. **Avoid Loose Clothing or Hair**: Do not wear ties or any loose, hanging clothing. Ensure that ponytails are not left down and that there are no loose strands of hair. Bundle up long hair securely.
2. **No Jewelry**: Do not wear necklaces, rings, or other jewelry that could get caught in moving parts.
3. **Wear a Mechanic’s Jumpsuit**: Ideally, wear a mechanic’s jumpsuit as it is durable, comfortable, has pockets for tools, and has nothing loose that can get caught and pulled into moving parts.
4. **Always Wear Safety Goggles**: Always wear safety goggles for eye protection to avoid contact with splattering fluids.

Q:When and how to check engine oil level?

Ans:Engine oil should be checked each time the vehicle is refueled. Here are the steps to check the oil:

1. Turn the engine off.
2. Remove the dipstick, which typically has a yellow handle.
3. Wipe off the end of the dipstick with a rag or paper towel.
4. Put the dipstick back in.
5. Remove the dipstick again to look at the oil level at the tip.

The dipstick will have marks on it, and the "add" mark typically indicates one quart low.


Q:Below what temperature we need antifreeze washer fluid?

Ans:You need to use washer fluid with antifreeze if you live or travel in cold climates, below 32 degrees Fahrenheit.