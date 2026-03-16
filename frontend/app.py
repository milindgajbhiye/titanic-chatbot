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
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        color: #0d47a1;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #424242;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .section-header {
        font-size: 1.4rem;
        color: #1565c0;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
        font-weight: 600;
    }
    
    .description {
        font-size: 0.95rem;
        color: #666666;
        margin-bottom: 1.5rem;
        line-height: 1.6;
    }
    
    .button-text {
        font-weight: 600;
    }
    
    .response-box {
        background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%);
        padding: 1.5rem;
        border-left: 5px solid #0d47a1;
        border-radius: 8px;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="main-title">Titanic Explorer</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Uncover fascinating stories from the most legendary ship in history</div>',
    unsafe_allow_html=True
)

st.divider()

st.markdown('<div class="section-header">Let\'s Learn Together</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="description">This chatbot answers questions about Titanic passengers. Ask me anything about who traveled on this famous ship, how much they paid, or where they embarked from. Every answer comes directly from real historical data!</div>',
    unsafe_allow_html=True
)

input_col, button_col = st.columns([5, 1], gap="small")

with input_col:
    user_question = st.text_input(
        label="What would you like to know?",
        placeholder="E.g., How many male passengers were there?",
        label_visibility="collapsed"
    )

with button_col:
    ask_button = st.button("✨ Ask", use_container_width=True, key="ask_btn")

with st.expander("💡 Not sure what to ask? See examples"):
    st.markdown("""
    Try any of these questions:
    - What percentage of passengers were male?
    - What was the average ticket fare?
    - Where did passengers embark from?
    - How many passengers survived?
    - What was the survival rate?
    - How many passengers were in each class?
    - What percentage of passengers were female?
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
                    f'<div class="response-box"><strong>Answer:</strong><br>{answer}</div>',
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
