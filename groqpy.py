import streamlit as st
from groq import Groq


# Set your Groq API key (store in environment variable for security)
API_KEY = "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"
if not API_KEY:
    st.error("❌ API Key not found! Please set your GROQ_API_KEY environment variable.")
else:
    # Initialize Groq Client
    client = Groq(api_key=API_KEY)

    # Streamlit UI
    st.title("Chatbot with Groq API 🤖")

    # User input
    user_query = st.text_input("Ask me anything:")

    # Available models (Choose a valid one)
    MODEL_NAME = "llama-3.3-70b-versatile"  # Corrected model name

    # Process user query
    if st.button("Send"):
        if user_query:
            try:
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": user_query}],
                    model=MODEL_NAME,
                )
                response = chat_completion.choices[0].message.content
                st.write("🤖 **Chatbot:**", response)
            except Exception as e:
                st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠️ Please enter a message.")
