import os
from dotenv import load_dotenv
import streamlit as st
from model import Gem_Bookish,MessageContent
_bool = load_dotenv()

my_string = os.environ["GOOGLE_API_KEY"];

st.title("BookisH--your smart reading assistant!")
st.write("Your bibliophilic friend😊")


if "chat_assistant" not in st.session_state:
    st.session_state.chat_assistant = Gem_Bookish() 

#??This is to display the current running thread of conversation

if "messages" not in st.session_state:
     st.session_state.messages = []

for m in st.session_state.chat_assistant.get_message_history():
    with st.chat_message(m.role):
        st.markdown(m.msgstring)

if prompt := st.chat_input("Please Ask a Question"):
    with st.chat_message("user"):
         st.markdown(prompt)
         st.session_state.chat_assistant.chat_gemini(prompt)
        
 
       
   
    with st.spinner('Searching for answer'):
       
         response  = st.session_state.chat_assistant.get_answer()
                
    with st.chat_message("assistant"):
        st.markdown(response)
                      


   



    