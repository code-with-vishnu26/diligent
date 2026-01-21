import requests
import streamlit as st

# -----------------------------
# Local backend configuration
# -----------------------------
BACKEND_URL = "http://127.0.0.1:8000"
CHAT_ENDPOINT = f"{BACKEND_URL}/chat"

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Jarvis AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Jarvis AI")
st.caption("Local Self-Hosted Enterprise Copilot")

# -----------------------------
# Session state for chat memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display previous messages
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User input
# -----------------------------
user_query = st.chat_input("Ask Jarvis something...")

if user_query:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )
    with st.chat_message("user"):
        st.markdown(user_query)

    # Call local backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    CHAT_ENDPOINT,
                    json={"query": user_query},
                    timeout=60
                )

                if response.status_code == 200:
                    answer = response.json()["answer"]
                else:
                    answer = "⚠️ Backend returned an error."

            except Exception:
                answer = (
                    "❌ Could not connect to backend.\n\n"
                    "Make sure FastAPI is running at http://127.0.0.1:8000"
                )

            st.markdown(answer)

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("Local demo • FastAPI • Pinecone • RAG • Ollama")

