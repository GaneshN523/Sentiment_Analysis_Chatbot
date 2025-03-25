import streamlit as st
import nltk
from modules.chatbot import process_user_message

# Download the VADER lexicon (only needed on first run)
nltk.download('vader_lexicon')

st.title("Mental Health & Diagnosis Chatbot")
st.write(
    "Ask your health-related questions, describe your symptoms, or seek advice. "
    "Our system analyzes your input for sentiment and attempts a simple symptom diagnosis."
)

# Maintain chat history using Streamlit's session_state.
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input text widget.
user_input = st.text_input("You:", key="user_input")

# Process user input when the "Send" button is pressed.
if st.button("Send"):
    if user_input:
        response = process_user_message(user_input)
        st.session_state.chat_history.append({"user": user_input, "bot": response})
    else:
        st.warning("Please enter a message.")

# Display conversation history.
if st.session_state.chat_history:
    st.markdown("### Conversation")
    for chat in st.session_state.chat_history:
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**Bot:** {chat['bot']}")
        st.markdown("---")

st.write("To deploy this app, save the code and run it using:")
st.code("streamlit run app.py", language="bash")
