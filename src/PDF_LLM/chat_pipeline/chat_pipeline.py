from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def create_chat_pipeline(vectorstore, llm):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa_chain = ConversationalRetrievalChain(
        retriever=vectorstore.as_retriever(),
        llm=llm,
        memory=memory
    )
    return qa_chain
