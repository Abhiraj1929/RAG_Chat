import streamlit as st
from ui.styles import inject_styles
from ui.sidebar import render_sidebar
from ui.chat import render_chat
from core.vector_store import VectorStore

st.set_page_config(
    page_title="RAG Chat",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": None,
        "Report a Bug": None,
        "About": "RAG Chat - AI-powered document assistant",
    },
)

inject_styles()

if "vector_store" not in st.session_state:
    st.session_state.vector_store = VectorStore()

vector_store = st.session_state.vector_store

st.markdown(
    """
    <div class="app-header">
        <div class="logo">🤖</div>
        <div>
            <div class="title">RAG Chat</div>
            <div class="subtitle">AI-powered document assistant</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

render_sidebar(vector_store)
render_chat(vector_store)
