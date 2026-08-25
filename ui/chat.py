import streamlit as st
from core.vector_store import VectorStore
from core.rag_chain import get_rag_response


def render_chat(vector_store: VectorStore):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if not st.session_state.messages:
        _render_empty_state(vector_store)
    else:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if msg.get("sources"):
                    _render_sources(msg["sources"])

    if prompt := st.chat_input("Ask anything about your documents..."):
        _handle_message(prompt, vector_store)


def _render_empty_state(vector_store: VectorStore):
    has_docs = vector_store.count > 0

    if has_docs:
        st.markdown(
            """
            <div class="empty-state">
                <span class="empty-icon">&#10024;</span>
                <h2>Ready to answer!</h2>
                <p>Ask me anything about your uploaded documents.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        suggestions = [
            ("Summarize my documents", "Summarize the key points from my uploaded documents"),
            ("Find key insights", "What are the most important insights from my documents?"),
            ("Compare sections", "Compare and contrast different sections of my documents"),
        ]
    else:
        st.markdown(
            """
            <div class="empty-state">
                <span class="empty-icon">&#128196;</span>
                <h2>How can I help you today?</h2>
                <p>Upload documents, then ask me anything about them.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div style="text-align:center;margin:0.5rem 0 1rem;">
                <span style="display:inline-block;background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.2);border-radius:10px;padding:10px 20px;color:#60a5fa;font-size:0.85rem;">
                    &#128194; Open the <b>Sidebar</b> (top-left &#9776; or swipe right) to upload files
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        suggestions = [
            ("Upload a PDF", "I'll help you analyze your PDF document"),
            ("Paste some text", "I'll help you understand and answer questions about the text"),
            ("Ask a question", "Type your question in the chat box below"),
        ]

    cols = st.columns(min(len(suggestions), 3))
    for i, (label, _) in enumerate(suggestions):
        with cols[i]:
            if st.button(label, use_container_width=True, key=f"suggestion_{i}"):
                if has_docs:
                    _handle_message(
                        suggestions[i][1].replace("I'll help you ", "").lower(),
                        vector_store,
                    )
                else:
                    st.info("Click the menu in the top-left to open the sidebar and upload a document!", icon="📁")


def _render_sources(sources: list):
    if not sources:
        return

    with st.expander("View Sources", expanded=False):
        for src in sources[:5]:
            st.markdown(
                f"""<div class="source-card">
                    <div class="source-label">{src['source']} (similarity: {src['similarity']:.2f})</div>
                    <div>{src['content'][:300]}{'...' if len(src['content']) > 300 else ''}</div>
                </div>""",
                unsafe_allow_html=True,
            )


def _handle_message(prompt: str, vector_store: VectorStore):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        sources_placeholder = st.empty()

        try:
            response_stream, sources = get_rag_response(
                prompt, vector_store, st.session_state.messages
            )

            full_response = ""
            for chunk in response_stream:
                if chunk:
                    full_response += chunk
                    message_placeholder.markdown(full_response + "\u258c")

            message_placeholder.markdown(full_response)

            if sources:
                with sources_placeholder.expander("View Sources", expanded=False):
                    for src in sources[:5]:
                        st.markdown(
                            f"""<div class="source-card">
                                <div class="source-label">{src['source']} (similarity: {src['similarity']:.2f})</div>
                                <div>{src['content'][:300]}{'...' if len(src['content']) > 300 else ''}</div>
                            </div>""",
                            unsafe_allow_html=True,
                        )

        except Exception as e:
            full_response = f"Sorry, an error occurred: {e}"
            message_placeholder.error(full_response)
            sources = []

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response,
        "sources": sources if 'sources' in dir() else [],
    })
