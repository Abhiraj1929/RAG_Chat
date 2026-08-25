CSS = """
<style>
    /* ── Reset & Base ── */
    .stApp {
        background-color: #212121;
        color: #e5e5e5;
    }

    /* ── Hide Streamlit branding ── */
    #MainMenu, header, footer { visibility: hidden; }
    .stDeployButton { display: none; }

    /* ── Main container ── */
    .block-container {
        max-width: 1000px;
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }

    /* ── Header bar ── */
    .app-header {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 20px;
        background: #212121;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        margin: -1rem -1rem 1rem -1rem;
        position: sticky;
        top: 0;
        z-index: 100;
    }
    .app-header .logo {
        width: 36px;
        height: 36px;
        border-radius: 10px;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        color: white;
        font-weight: 700;
        flex-shrink: 0;
    }
    .app-header .title {
        font-size: 16px;
        font-weight: 600;
        color: #f5f5f5;
    }
    .app-header .subtitle {
        font-size: 11px;
        color: #888;
    }

    /* ── Chat messages ── */
    .stChatMessage {
        background: transparent !important;
        border: none !important;
        padding: 0.5rem 0 !important;
    }
    div[data-testid="stChatMessageContent"] {
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* User bubble */
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
        background: transparent !important;
    }
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) div[data-testid="stChatMessageContent"] {
        background: #2f2f2f;
        border-radius: 18px 18px 4px 18px;
        padding: 10px 16px;
        display: inline-block;
        max-width: 80%;
        float: right;
        clear: both;
    }

    /* Assistant */
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
        background: transparent !important;
    }
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) div[data-testid="stChatMessageContent"] {
        padding: 10px 0;
    }

    /* ── Chat input ── */
    div[data-testid="stChatInput"] {
        background: #2f2f2f !important;
        border-radius: 24px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        padding: 4px !important;
    }
    div[data-testid="stChatInput"] textarea {
        font-size: 0.95rem !important;
        padding: 8px 14px !important;
    }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background-color: #1a1a1a !important;
        border-right: 1px solid rgba(255,255,255,0.08) !important;
    }
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #e5e5e5 !important;
    }

    /* ── File uploader ── */
    .stFileUploader {
        border: 2px dashed rgba(255,255,255,0.12) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        transition: border-color 0.2s !important;
    }
    .stFileUploader:hover {
        border-color: rgba(59,130,246,0.5) !important;
    }
    .stFileUploader label {
        color: #999 !important;
        font-size: 0.85rem !important;
    }

    /* ── Buttons ── */
    .stButton > button {
        border-radius: 10px !important;
        font-weight: 500 !important;
        transition: all 0.15s !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #e5e5e5 !important;
        background: transparent !important;
    }
    .stButton > button:hover {
        background: rgba(255,255,255,0.08) !important;
        border-color: rgba(255,255,255,0.2) !important;
    }
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: #3b82f6 !important;
        border-color: #3b82f6 !important;
        color: white !important;
    }
    .stButton > button[kind="primary"]:hover,
    .stButton > button[data-testid="stBaseButton-primary"]:hover {
        background: #2563eb !important;
    }

    /* ── Success / Error boxes ── */
    .upload-success {
        background: rgba(34,197,94,0.08);
        border: 1px solid rgba(34,197,94,0.2);
        border-radius: 10px;
        padding: 10px 14px;
        color: #4ade80;
        font-size: 0.85rem;
    }
    .upload-error {
        background: rgba(239,68,68,0.08);
        border: 1px solid rgba(239,68,68,0.2);
        border-radius: 10px;
        padding: 10px 14px;
        color: #f87171;
        font-size: 0.85rem;
    }

    /* ── Source cards ── */
    .source-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 10px;
        padding: 10px 14px;
        margin-top: 6px;
        font-size: 0.8rem;
        color: #aaa;
    }
    .source-card .source-label {
        color: #3b82f6;
        font-weight: 600;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }

    /* ── Suggestion cards ── */
    .suggestion-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 14px 18px;
        cursor: pointer;
        transition: all 0.15s;
        color: #ccc;
        font-size: 0.9rem;
    }
    .suggestion-card:hover {
        background: rgba(255,255,255,0.08);
        border-color: rgba(59,130,246,0.4);
        color: #fff;
    }
    .suggestion-card .suggestion-icon {
        font-size: 1.1rem;
        margin-bottom: 6px;
    }

    /* ── Empty state ── */
    .empty-state {
        text-align: center;
        padding: 4rem 2rem;
        color: #888;
    }
    .empty-state h2 {
        color: #e5e5e5;
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 1rem;
    }
    .empty-state p {
        color: #999;
        font-size: 0.95rem;
        margin-top: 0.5rem;
    }

    /* ── Badge ── */
    .badge {
        display: inline-block;
        background: rgba(59,130,246,0.15);
        color: #60a5fa;
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 500;
    }

    /* ── Responsive ── */
    @media (max-width: 768px) {
        .block-container {
            padding: 0.5rem !important;
        }
        .app-header {
            padding: 10px 14px;
        }
        .app-header .logo {
            width: 32px;
            height: 32px;
            font-size: 16px;
        }
        .app-header .title {
            font-size: 14px;
        }
        div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) div[data-testid="stChatMessageContent"] {
            max-width: 90%;
        }
    }

    /* ── Textarea ── */
    .stTextArea textarea {
        background: #2f2f2f !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        color: #e5e5e5 !important;
    }
    .stTextArea textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 1px #3b82f6 !important;
    }

    /* ── Divider ── */
    hr {
        border-color: rgba(255,255,255,0.08) !important;
        margin: 1rem 0 !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-top-color: #3b82f6 !important;
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        color: #888 !important;
        border-radius: 8px 8px 0 0;
    }
    .stTabs [aria-selected="true"] {
        color: #e5e5e5 !important;
        background: #2f2f2f !important;
    }
</style>
"""


def inject_styles():
    import streamlit as st
    st.markdown(CSS, unsafe_allow_html=True)
