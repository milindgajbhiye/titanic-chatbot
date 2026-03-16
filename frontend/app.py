import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Titanic Explorer",
    page_icon="🚢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    
    <style>
    :root {
        --bg-1: #f3f8ff;
        --bg-2: #fef6e4;
        --surface: #ffffff;
        --surface-soft: #f7fbff;
        --text-main: #1b2a41;
        --text-muted: #4f5d75;
        --primary: #0a5ea8;
        --primary-strong: #084b86;
        --accent: #f59e0b;
        --success-bg: #e6f9f0;
        --warning-bg: #fff6e6;
        --danger-bg: #ffe9e9;
        --border: #d9e4f2;
    }

    * {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(1100px 520px at -8% -20%, rgba(10, 94, 168, 0.18), transparent 62%),
            radial-gradient(900px 500px at 110% 10%, rgba(245, 158, 11, 0.22), transparent 58%),
            linear-gradient(160deg, var(--bg-1) 0%, var(--bg-2) 100%);
    }

    .block-container {
        max-width: 860px;
        padding-top: 2.2rem;
        padding-bottom: 2.6rem;
    }

    .page-shell {
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 1.3rem 1.3rem 1.6rem;
        box-shadow: 0 18px 50px rgba(19, 42, 86, 0.12);
        backdrop-filter: blur(4px);
    }

    @media (max-width: 768px) {
        .page-shell {
            border-radius: 16px;
            padding: 1rem 0.9rem 1.2rem;
        }
    }
    
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(2rem, 5vw, 3.2rem);
        color: var(--text-main);
        text-align: left;
        margin-bottom: 0.25rem;
        letter-spacing: -1px;
        line-height: 1.1;
    }

    .hero-chip {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        background: rgba(10, 94, 168, 0.1);
        color: var(--primary-strong);
        border: 1px solid rgba(10, 94, 168, 0.26);
        padding: 0.3rem 0.8rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.7rem;
    }
    
    .subtitle {
        font-size: 1rem;
        color: var(--text-muted);
        text-align: left;
        margin-bottom: 1.2rem;
        font-weight: 400;
        line-height: 1.7;
    }
    
    .section-header {
        font-size: 1.2rem;
        color: var(--primary-strong);
        margin-top: 1.2rem;
        margin-bottom: 0.6rem;
        font-weight: 600;
    }
    
    .description {
        font-size: 0.98rem;
        color: var(--text-muted);
        margin-bottom: 1rem;
        line-height: 1.65;
        background: var(--surface-soft);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 0.9rem 1rem;
    }

    .input-caption {
        font-size: 0.86rem;
        color: #5f6f88;
        margin-top: -0.2rem;
        margin-bottom: 0.45rem;
        font-weight: 500;
    }

    .stTextInput > div > div > input {
        border: 1px solid #c9d8ea;
        border-radius: 12px;
        padding: 0.72rem 0.9rem;
        font-size: 0.98rem;
        color: var(--text-main);
        background: #ffffff;
    }

    .stTextInput > div > div > input:focus {
        border-color: var(--primary);
        box-shadow: 0 0 0 3px rgba(10, 94, 168, 0.17);
    }

    .stButton > button {
        border-radius: 12px;
        border: 0;
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-strong) 100%);
        color: white;
        font-weight: 600;
        min-height: 2.8rem;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
        box-shadow: 0 8px 18px rgba(8, 75, 134, 0.25);
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 10px 22px rgba(8, 75, 134, 0.3);
    }

    .stButton > button:focus {
        box-shadow: 0 0 0 3px rgba(10, 94, 168, 0.2);
    }

    .stExpander {
        border: 1px solid var(--border);
        border-radius: 12px;
        background: #fbfdff;
    }

    .stAlert {
        border-radius: 12px;
        border: 1px solid var(--border);
    }
    
    .response-box {
        background: linear-gradient(135deg, #f1f7ff 0%, #fff8ec 100%);
        padding: 1rem 1.1rem;
        border: 1px solid #cfe0f5;
        border-left: 5px solid var(--primary);
        border-radius: 14px;
        margin-top: 0.6rem;
        color: var(--text-main);
        line-height: 1.55;
    }

    .answer-title {
        font-size: 0.92rem;
        color: var(--primary-strong);
        font-weight: 700;
        margin-bottom: 0.3rem;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

    .footer-note {
        text-align: center;
        color: #65748d;
        font-size: 0.84rem;
        margin-top: 1.4rem;
    }

    [data-testid="stDivider"] {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-shell">', unsafe_allow_html=True)

st.markdown('<div class="hero-chip">Data Storytelling · Real Titanic Records</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Titanic Explorer</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Ask natural questions about passenger demographics, fares, classes, embarkation, and survival outcomes. The assistant responds using the original historical dataset.</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="section-header">Ask A Question</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="description">Use specific questions for best results, like counts, averages, percentages, class-wise comparisons, or distribution plots.</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="input-caption">Type your question below</div>', unsafe_allow_html=True)

input_col, button_col = st.columns([5, 1.3], gap="small")

with input_col:
    user_question = st.text_input(
        label="What would you like to know?",
        placeholder="Try: What percentage of passengers survived?",
        label_visibility="collapsed"
    )

with button_col:
    st.markdown("<div style='height: 1px;'></div>", unsafe_allow_html=True)
    ask_button = st.button("Ask", use_container_width=True, key="ask_btn")

with st.expander("Need ideas? Start with one of these"):
    st.markdown("""
    - How many passengers were on the Titanic?
    - What percentage of passengers were male?
    - What percentage of passengers survived?
    - What was the average ticket fare?
    - How many passengers were in each class?
    - Where did passengers embark from?
    - How many passengers were children?
    - Show me the age histogram
    """)

st.divider()

if ask_button:
    if not user_question.strip():
        st.warning("🤔 Please type a question first!")
    
    else:
        try:
            with st.spinner("🔍 Searching through historical records..."):
                server_response = requests.post(
                    f"{BACKEND_URL}/ask",
                    json={"question": user_question},
                    timeout=5
                )

            if server_response.status_code == 200:
                response_data = server_response.json()
                answer = response_data['answer']

                st.success("✅ Found the answer!")
                st.markdown(
                    f'<div class="response-box"><div class="answer-title">Answer</div>{answer}</div>',
                    unsafe_allow_html=True
                )

                if "image" in response_data:
                    import base64
                    from PIL import Image
                    import io

                    image_bytes = base64.b64decode(response_data["image"])
                    image = Image.open(io.BytesIO(image_bytes))

                    st.markdown("<br>", unsafe_allow_html=True)
                    st.image(image, use_container_width=True)

            else:
                st.error("😕 The server returned an error. Try rephrasing your question!")
        
        except requests.exceptions.ConnectionError:
            st.error(f"❌ Can't connect to the backend server. Make sure it's running on {BACKEND_URL}")
        
        except requests.exceptions.Timeout:
            st.error("⏱️ The request took too long. Please try again!")
        
        except Exception as error:
            st.error(f"⚠️ Something went wrong: {str(error)}")

st.markdown('<div class="footer-note">Built with Streamlit + FastAPI · Titanic Dataset (891 passengers)</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
