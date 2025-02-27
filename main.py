from streamlit import session_state

from backend.core import run_llm
import streamlit as st
from typing import Set

# Configure the theme to match LangChain's style
st.set_page_config(
    page_title="Documentation Helper Bot",
    page_icon="🔗",
    layout="wide"
)

# Custom CSS to match LangChain's theme
st.markdown("""
    <style>
    /* Main background and text colors */
    .stApp {
        background-color: white;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Button colors */
    .stButton>button {
        background-color: #1D3B36;
        color: white;
        border: none;
        border-radius: 40px;
        padding: 0.5rem 1rem;
    }
    
    .stButton>button:hover {
        background-color: #2B5750;
        border: none;
    }
    
    /* Form submit button - special styling */
    .stFormSubmitButton>button {
        background-color: #C5B7FF;
        color: #1D3B36;
    }
    
    /* Headers styling */
    h1, h2, h3 {
        color: #1D3B36;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for user information
with st.sidebar:
    st.title("User Profile")
    
    # Profile picture upload
    profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "jpeg", "png"])
    if profile_pic:
        st.image(profile_pic, width=200)
    else:
        # Display default avatar if no image is uploaded
        st.image("https://www.w3schools.com/howto/img_avatar.png", width=200)
    
    # User information form
    with st.form("user_info"):
        name = st.text_input("Name", key="user_name")
        email = st.text_input("Email", key="user_email")
        submit = st.form_submit_button("Save Profile")
        
        if submit:
            st.success("Profile updated successfully!")

st.header("Documentation Helper Bot")

prompt = st.text_input("Prompt", placeholder="Enter your Prompt here..")

if (
    "chat_answer_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state
):
    st.session_state["chat_answer_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []

def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string

if prompt:
    with st.spinner("Generating response.."):
        generated_response = run_llm(
            query=prompt, chat_history=st.session_state["chat_history"]
        )
        sources = set([doc.metadata["source"] for doc in generated_response["source_documents"]])

        formatted_response = f"{generated_response['result']} \n\n {create_sources_string(sources)}"
        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answer_history"].append(formatted_response)
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", generated_response["result"]))

if st.session_state["chat_answer_history"]:
    for generated_response, user_query in zip(st.session_state["chat_answer_history"], st.session_state["user_prompt_history"]):
        st.chat_message("user").write(user_query)
        st.chat_message("assistant").write(generated_response)

