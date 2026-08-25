from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from core.vector_store import VectorStore
from config import OPENROUTER_API_KEY, CHAT_MODEL

SYSTEM_PROMPT = """You are a helpful AI assistant for a RAG (Retrieval-Augmented Generation) chat platform.
Answer the user's question based on the provided context documents.
If the context doesn't contain enough information to answer, say so honestly.
Always cite which document(s) you used when possible.
Be concise and accurate."""

prompt = ChatPromptTemplate.from_messages([
    ("system", f"{SYSTEM_PROMPT}\n\n## Retrieved Context\n{{context}}"),
    ("human", "{question}"),
])


def get_llm():
    return ChatOpenAI(
        model=CHAT_MODEL,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1",
        streaming=True,
        temperature=0.3,
    )


def format_docs(docs: list) -> str:
    formatted = []
    for i, (doc, sim) in enumerate(docs):
        source = doc.metadata.get("source", "unknown")
        formatted.append(
            f"[Document {i + 1}] (source: {source}, similarity: {sim:.2f})\n{doc.page_content}"
        )
    return "\n\n---\n\n".join(formatted) if formatted else "No relevant documents found."


def get_rag_response(question: str, vector_store: VectorStore, chat_history: list = None):
    context_docs = vector_store.search(question, k=5, threshold=0.3)
    context = format_docs(context_docs)

    llm = get_llm()
    chain = prompt | llm | StrOutputParser()

    history_text = ""
    if chat_history:
        for msg in chat_history[-6:]:
            role = "User" if msg["role"] == "user" else "Assistant"
            history_text += f"{role}: {msg['content']}\n"

    input_data = {
        "context": context,
        "question": question,
    }

    if history_text:
        input_data["question"] = f"Previous conversation:\n{history_text}\nCurrent question: {question}"

    sources = [{"content": doc.page_content, "source": doc.metadata.get("source", "unknown"), "similarity": sim} for doc, sim in context_docs]

    return chain.stream(input_data), sources
