import streamlit as st
from core.vector_store import VectorStore
from core.rag_chain import get_rag_response


def render_chat(vector_store: VectorStore):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if not st.session_state.messages:
        _render_empty_state()
        return

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                _render_sources(msg["sources"])

    if prompt := st.chat_input("Ask anything..."):
        _handle_message(prompt, vector_store)


def _render_empty_state():
    st.markdown(
        """
        <div class="empty-state">
            <div style="font-size: 2.5rem;">&#10024;</div>
            <h2>How can I help you today?</h2>
            <p>Upload documents in the sidebar, then ask me anything about them.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    suggestions = [
        ("Summarize my documents", "Summarize the key points from my uploaded documents"),
        ("Find key insights", "What are the most important insights from my documents?"),
        ("Compare sections", "Compare and contrast different sections of my documents"),
    ]

    for col, (label, query) in zip(cols, suggestions):
        with col:
            if st.button(label, use_container_width=True, key=f"suggestion_{label}"):
                _handle_message(query, st.session_state.vector_store)


def _render_sources(sources: list):
    if not sources:
        return

    with st.expander("Sources", expanded=False):
        for src in sources[:3]:
            st.markdown(
                f"""<div class="source-card">
                    <div class="source-label">{src['source']} (similarity: {src['similarity']:.2f})</div>
                    <div>{src['content'][:200]}{'...' if len(src['content']) > 200 else ''}</div>
                </div>""",
                unsafe_allow_html=True,
            )


def _handle_message(prompt: str, vector_store: VectorStore):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response_stream, sources = get_rag_response(
                    prompt, vector_store, st.session_state.messages
                )
                response = st.write_stream(response_stream)
            except Exception as e:
                response = f"Error: {e}"
                st.error(response)
                sources = []

        if response:
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "sources": sources,
            })
            _render_sources(sources)
