from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma


#load pdf
loader = PyPDFLoader("notes.pdf")
documents = loader.load()

print(f"Loaded {len(documents)} pages.")


#spliting pdf into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks.")


#create embeddings using Ollama
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


#store embeddings in chroma
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="my_pdf"
)


#create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)


#create local LLM
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


#ask questions
while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    # Retrieve relevant chunks
    relevant_docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in relevant_docs
    )

    prompt = f"""
You are answering questions about a PDF.

Use ONLY the information provided in the context below.

If the answer is not present in the context, say:
"I cannot find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    print("\nANSWER:")
    print(response.content)

    print("\nSOURCES:")

    for doc in relevant_docs:
        page = doc.metadata.get("page", "unknown")
        print(f"- Page {page + 1}")