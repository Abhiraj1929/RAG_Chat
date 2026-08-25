CSS = """
<style>
    /* ══════════════════════════════════════════
       RESET & BASE
       ══════════════════════════════════════════ */
    .stApp {
        background-color: #212121;
        color: #e5e5e5;
        min-height: 100vh;
    }

    #MainMenu, header, footer { visibility: hidden; }
    .stDeployButton { display: none; }

    /* Hide scrollbar globally */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.2); }

    /* ══════════════════════════════════════════
       MAIN CONTAINER
       ══════════════════════════════════════════ */
    .block-container {
        max-width: 900px !important;
        padding-top: 0.5rem !important;
        padding-bottom: 1rem !important;
        margin: 0 auto;
    }

    /* ══════════════════════════════════════════
       HEADER
       ══════════════════════════════════════════ */
    .app-header {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px 24px;
        background: #171717;
        border-bottom: 1px solid rgba(255,255,255,0.06);
        margin: 0 -1rem 0.5rem -1rem;
        position: sticky;
        top: 0;
        z-index: 100;
        backdrop-filter: blur(10px);
    }
    .app-header .logo {
        width: 38px;
        height: 38px;
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
        font-size: 17px;
        font-weight: 600;
        color: #f5f5f5;
        letter-spacing: -0.01em;
    }
    .app-header .subtitle {
        font-size: 12px;
        color: #777;
        margin-top: 1px;
    }

    /* ══════════════════════════════════════════
       CHAT MESSAGES
       ══════════════════════════════════════════ */
    .stChatMessage {
        background: transparent !important;
        border: none !important;
        padding: 0.75rem 0 !important;
        max-width: 100% !important;
    }
    div[data-testid="stChatMessageContent"] {
        font-size: 0.93rem;
        line-height: 1.65;
        word-wrap: break-word;
        overflow-wrap: break-word;
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

    /* ══════════════════════════════════════════
       CHAT INPUT - always visible at bottom
       ══════════════════════════════════════════ */
    div[data-testid="stChatInput"] {
        background: #2f2f2f !important;
        border-radius: 24px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        padding: 4px 8px !important;
        margin: 0 !important;
    }
    div[data-testid="stChatInput"]:focus-within {
        border-color: rgba(59,130,246,0.5) !important;
        box-shadow: 0 0 0 1px rgba(59,130,246,0.3) !important;
    }
    div[data-testid="stChatInput"] textarea {
        font-size: 0.95rem !important;
        padding: 10px 14px !important;
        min-height: 24px !important;
    }
    div[data-testid="stChatInput"] button[data-testid="stChatInputActionButton"] {
        background: #3b82f6 !important;
        border-radius: 50% !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
        min-height: 36px !important;
    }

    /* ══════════════════════════════════════════
       SIDEBAR
       ══════════════════════════════════════════ */
    section[data-testid="stSidebar"] {
        background-color: #171717 !important;
        border-right: 1px solid rgba(255,255,255,0.06) !important;
    }
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #e5e5e5 !important;
    }
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: #aaa !important;
    }

    /* ══════════════════════════════════════════
       FILE UPLOADER
       ══════════════════════════════════════════ */
    .stFileUploader {
        border: 2px dashed rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        transition: all 0.2s !important;
    }
    .stFileUploader:hover {
        border-color: rgba(59,130,246,0.4) !important;
        background: rgba(59,130,246,0.03) !important;
    }
    .stFileUploader label {
        color: #999 !important;
        font-size: 0.85rem !important;
    }
    .stFileUploader [data-testid="stFileUploaderDropzone"] {
        background: transparent !important;
        border: none !important;
    }

    /* ══════════════════════════════════════════
       BUTTONS
       ══════════════════════════════════════════ */
    .stButton > button {
        border-radius: 10px !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        transition: all 0.15s !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #e5e5e5 !important;
        background: transparent !important;
        padding: 0.5rem 1rem !important;
        min-height: 40px !important;
    }
    .stButton > button:hover {
        background: rgba(255,255,255,0.08) !important;
        border-color: rgba(255,255,255,0.2) !important;
    }
    .stButton > button:active {
        transform: scale(0.98);
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
        border-color: #2563eb !important;
    }

    /* ══════════════════════════════════════════
       TEXTAREA
       ══════════════════════════════════════════ */
    .stTextArea textarea {
        background: #2f2f2f !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        color: #e5e5e5 !important;
        font-size: 0.9rem !important;
    }
    .stTextArea textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 1px #3b82f6 !important;
    }

    /* ══════════════════════════════════════════
       TABS
       ══════════════════════════════════════════ */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0 !important;
        background: transparent !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #888 !important;
        border-radius: 8px 8px 0 0 !important;
        font-size: 0.85rem !important;
        padding: 8px 16px !important;
    }
    .stTabs [aria-selected="true"] {
        color: #e5e5e5 !important;
        background: #2f2f2f !important;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #3b82f6 !important;
    }

    /* ══════════════════════════════════════════
       BADGE
       ══════════════════════════════════════════ */
    .badge {
        display: inline-block;
        background: rgba(59,130,246,0.15);
        color: #60a5fa;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 500;
    }

    /* ══════════════════════════════════════════
       EMPTY STATE
       ══════════════════════════════════════════ */
    .empty-state {
        text-align: center;
        padding: 3rem 1.5rem 2rem;
        color: #888;
    }
    .empty-state .empty-icon {
        font-size: 3rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    .empty-state h2 {
        color: #e5e5e5;
        font-size: 1.4rem;
        font-weight: 600;
        margin: 0.5rem 0;
    }
    .empty-state p {
        color: #999;
        font-size: 0.9rem;
        margin-top: 0.25rem;
    }

    /* ══════════════════════════════════════════
       SOURCE CARDS
       ══════════════════════════════════════════ */
    .source-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 10px;
        padding: 10px 14px;
        margin-top: 6px;
        font-size: 0.8rem;
        color: #aaa;
        word-wrap: break-word;
    }
    .source-card .source-label {
        color: #3b82f6;
        font-weight: 600;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }

    /* ══════════════════════════════════════════
       SUGGESTION CHIPS
       ══════════════════════════════════════════ */
    .suggestion-chip {
        display: inline-block;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 8px 16px;
        color: #bbb;
        font-size: 0.85rem;
        cursor: pointer;
        transition: all 0.15s;
        margin: 4px;
    }
    .suggestion-chip:hover {
        background: rgba(59,130,246,0.1);
        border-color: rgba(59,130,246,0.3);
        color: #e5e5e5;
    }

    /* ══════════════════════════════════════════
       DIVIDER
       ══════════════════════════════════════════ */
    hr {
        border-color: rgba(255,255,255,0.06) !important;
        margin: 0.75rem 0 !important;
    }

    /* ══════════════════════════════════════════
       ALERTS
       ══════════════════════════════════════════ */
    .stAlert {
        border-radius: 10px !important;
    }

    /* ══════════════════════════════════════════
       EXPANDER
       ══════════════════════════════════════════ */
    .streamlit-expanderHeader {
        font-size: 0.85rem !important;
        color: #aaa !important;
    }

    /* ══════════════════════════════════════════
       SPINNER
       ══════════════════════════════════════════ */
    .stSpinner > div {
        border-top-color: #3b82f6 !important;
    }

    /* ══════════════════════════════════════════
       MOBILE: < 768px
       ══════════════════════════════════════════ */
    @media (max-width: 768px) {
        .block-container {
            padding: 0 !important;
            max-width: 100% !important;
        }

        .app-header {
            padding: 12px 16px;
            gap: 10px;
        }
        .app-header .logo {
            width: 34px;
            height: 34px;
            font-size: 16px;
        }
        .app-header .title {
            font-size: 15px;
        }
        .app-header .subtitle {
            font-size: 11px;
        }

        /* Chat messages */
        div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) div[data-testid="stChatMessageContent"] {
            max-width: 88%;
            padding: 8px 14px;
        }
        div[data-testid="stChatMessageContent"] {
            font-size: 0.9rem;
        }

        /* Chat input full width on mobile */
        div[data-testid="stChatInput"] {
            margin: 0 8px !important;
            border-radius: 20px !important;
        }

        /* Empty state */
        .empty-state {
            padding: 2rem 1rem;
        }
        .empty-state .empty-icon {
            font-size: 2.5rem;
        }
        .empty-state h2 {
            font-size: 1.2rem;
        }

        /* Sidebar mobile overlay */
        section[data-testid="stSidebar"] {
            width: 85vw !important;
            max-width: 340px !important;
        }
        section[data-testid="stSidebar"] > div {
            padding: 1rem !important;
        }

        /* Tabs */
        .stTabs [data-baseweb="tab"] {
            font-size: 0.8rem !important;
            padding: 6px 12px !important;
        }

        /* Buttons full width */
        .stButton {
            width: 100% !important;
        }
        .stButton > button {
            width: 100% !important;
        }

        /* File uploader */
        .stFileUploader {
            padding: 0.75rem !important;
        }
    }

    /* ══════════════════════════════════════════
       TABLET: 769px - 1024px
       ══════════════════════════════════════════ */
    @media (min-width: 769px) and (max-width: 1024px) {
        .block-container {
            max-width: 95% !important;
        }
    }

    /* ══════════════════════════════════════════
       SMALL MOBILE: < 480px
       ══════════════════════════════════════════ */
    @media (max-width: 480px) {
        .app-header {
            padding: 10px 12px;
        }
        .app-header .logo {
            width: 30px;
            height: 30px;
            font-size: 14px;
            border-radius: 8px;
        }
        .app-header .title {
            font-size: 14px;
        }
        .app-header .subtitle {
            display: none;
        }

        div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) div[data-testid="stChatMessageContent"] {
            max-width: 92%;
            font-size: 0.85rem;
        }

        .empty-state {
            padding: 1.5rem 0.75rem;
        }
        .empty-state h2 {
            font-size: 1.1rem;
        }
        .empty-state p {
            font-size: 0.82rem;
        }
    }

    /* ══════════════════════════════════════════
       LANDSCAPE MOBILE
       ══════════════════════════════════════════ */
    @media (max-height: 500px) and (orientation: landscape) {
        .empty-state {
            padding: 1rem;
        }
        .empty-state .empty-icon {
            font-size: 1.5rem;
        }
        .empty-state h2 {
            font-size: 1rem;
            margin: 0.25rem 0;
        }
    }

    /* ══════════════════════════════════════════
       SAFE AREA (notch devices)
       ══════════════════════════════════════════ */
    @supports (padding: env(safe-area-inset-top)) {
        .app-header {
            padding-top: calc(14px + env(safe-area-inset-top));
            padding-left: calc(24px + env(safe-area-inset-left));
            padding-right: calc(24px + env(safe-area-inset-right));
        }
        div[data-testid="stChatInput"] {
            padding-bottom: env(safe-area-inset-bottom) !important;
        }
    }
</style>
"""


def inject_styles():
    import streamlit as st
    st.markdown(CSS, unsafe_allow_html=True)
