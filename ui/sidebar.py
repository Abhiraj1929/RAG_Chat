import streamlit as st
from core.document_processor import process_file, process_text
from core.vector_store import VectorStore


def render_sidebar(vector_store: VectorStore):
    with st.sidebar:
        st.markdown("### Knowledge Base")
        st.markdown(
            f'<span class="badge">{vector_store.count} chunks indexed</span>',
            unsafe_allow_html=True,
        )
        st.markdown("---")

        tab_upload, tab_paste = st.tabs(["Upload File", "Paste Text"])

        with tab_upload:
            uploaded_file = st.file_uploader(
                "Drop a file here",
                type=["pdf", "txt", "md", "csv", "json"],
                label_visibility="collapsed",
                key="file_uploader",
            )

            if uploaded_file:
                with st.spinner("Processing document..."):
                    try:
                        chunks = process_file(uploaded_file, uploaded_file.name)
                        added = vector_store.add_documents(chunks)
                        st.success(f"Ingested **{added}** chunks from `{uploaded_file.name}`")
                    except Exception as e:
                        st.error(f"Error: {e}")

        with tab_paste:
            text_input = st.text_area(
                "Paste your text here...",
                height=120,
                label_visibility="collapsed",
                key="text_input",
            )
            if st.button("Ingest Text", use_container_width=True, type="primary"):
                if text_input.strip():
                    with st.spinner("Processing text..."):
                        try:
                            chunks = process_text(text_input.strip())
                            added = vector_store.add_documents(chunks)
                            st.success(f"Ingested **{added}** chunks")
                        except Exception as e:
                            st.error(f"Error: {e}")
                else:
                    st.warning("Please enter some text first.")

        st.markdown("---")
        if vector_store.count > 0:
            if st.button("Clear Knowledge Base", use_container_width=True):
                vector_store.clear()
                st.success("Knowledge base cleared.")
                st.rerun()
