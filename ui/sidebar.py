import streamlit as st
from core.document_processor import process_file, process_text
from core.vector_store import VectorStore


def render_sidebar(vector_store: VectorStore):
    with st.sidebar:
        st.markdown("### Knowledge Base")

        st.markdown(
            '<p style="color:#666;font-size:0.78rem;margin:-4px 0 8px 0;">Upload files or paste text, then chat below</p>',
            unsafe_allow_html=True,
        )

        count = vector_store.count
        if count > 0:
            st.markdown(
                f'<span class="badge">{count} chunks indexed</span>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<span class="badge" style="background:rgba(255,255,255,0.05);color:#888;">No documents yet</span>',
                unsafe_allow_html=True,
            )

        st.markdown("---")

        tab_upload, tab_paste = st.tabs(["Upload File", "Paste Text"])

        with tab_upload:
            st.markdown(
                '<p style="color:#999;font-size:0.82rem;margin-bottom:8px;">Supports PDF, TXT, MD, CSV, JSON</p>',
                unsafe_allow_html=True,
            )
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
                        st.success(f"Added **{added}** chunks from `{uploaded_file.name}`")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")

        with tab_paste:
            text_input = st.text_area(
                "Paste your text here...",
                height=140,
                label_visibility="collapsed",
                key="text_input",
                placeholder="Paste or type your document content here...",
            )
            if st.button("Ingest Text", use_container_width=True, type="primary", key="ingest_text_btn"):
                if text_input.strip():
                    with st.spinner("Processing text..."):
                        try:
                            chunks = process_text(text_input.strip())
                            added = vector_store.add_documents(chunks)
                            st.success(f"Added **{added}** chunks")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error: {e}")
                else:
                    st.warning("Please enter some text first.")

        st.markdown("---")

        if count > 0:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(
                    f'<p style="color:#888;font-size:0.8rem;margin:8px 0 0 0;">{count} chunks ready</p>',
                    unsafe_allow_html=True,
                )
            with col2:
                if st.button("Clear", key="clear_kb_btn", help="Clear all documents"):
                    vector_store.clear()
                    st.session_state.messages = []
                    st.success("Cleared!")
                    st.rerun()
