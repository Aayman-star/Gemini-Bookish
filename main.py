import streamlit as st
from model import Gem_Bookish,MessageContent


st.title("BookisH--your smart reading assistant!")
st.write("Your bibliophilic friend😊")


if "gemini_assistant" not in st.session_state:
    st.session_state.gemini_assistant = Gem_Bookish()  ##class Gem_Bookish being initialised

#??This is to display the current running thread of conversation

if "messages" not in st.session_state:
     st.session_state.messages = []

for m in st.session_state.gemini_assistant.get_message_history():
    with st.chat_message(m.role):
        st.markdown(m.msgstring)

if prompt := st.chat_input("Say something..."):
    with st.chat_message("user"):
         st.markdown(prompt)
         st.session_state.gemini_assistant.chat_gemini(prompt) ##user question being passed to the models
        
 
       
   
    with st.spinner('Searching for answer'):
       
         response  = st.session_state.gemini_assistant.get_answer() ##response from the model
                
    with st.chat_message("assistant"):
        st.markdown(response)
                      


   



    