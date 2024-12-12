from src.data_ingestion.extract_text import extract_text_from_pdf
from src.data_transformation.preprocess import chunk_text
from src.data_transformation.embeddings import create_embeddings
from src.model.setup_llm import setup_llm
from src.chat_pipeline.chat_pipeline import create_chat_pipeline

def main():
    pdf_path = "data/pdfs/example.pdf"  # Path to the PDF file
    text = extract_text_from_pdf(pdf_path)
    
    text_chunks = chunk_text(text)
    vectorstore = create_embeddings(text_chunks)
    
    llm = setup_llm()
    chat_pipeline = create_chat_pipeline(vectorstore, llm)

    print("Chat with your PDF! (type 'exit' to quit)")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        response = chat_pipeline.run({"question": query})
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
