from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.chains import RetrievalQA

# Sample documents
documents = [
    "Python is a high-level programming language.",
    "Paris is the capital of France.",
    "The moon orbits the Earth.",
    "Football is a popular sport."
]

# Step 1: Create embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 2: Create FAISS vector store
faiss_index = FAISS.from_texts(documents, embedding=embedding_model)

# Step 3: Get user query
query = input("Enter your question: ")

# Step 4: Retrieve relevant documents
retriever = faiss_index.as_retriever()
relevant_docs = retriever.get_relevant_documents(query)

# Step 5: Build prompt from relevant content
context = "\n".join([doc.page_content for doc in relevant_docs])
prompt = f"""Use the following context to answer the question.

Context:
{context}

Question: {query}
"""

# Step 6: Use LLM (you can plug in HuggingFace or OpenAI)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Step 7: Invoke the model
response = llm.invoke([HumanMessage(content=prompt)])

print("Answer:", response.content)
