import os
from typing import Any
from dotenv import load_dotenv
import google.generativeai as genai


##Loading the api key from the .env file
api_key = os.getenv("GOOGLE_API_KEY")
#print(api_key)

genai.configure()

#configurations
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}
#safety settings
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

#system_instructions
system_instruction = """Act as a wise curator of a global collection of books and a knowledgeable reader providing valuable 
information and sharing useful insights about the books and authors the user asks about."""

"""
Initializing the message class for message display
"""
class MessageContent:
    def __init__(self,role:str,msgstring:str| Any):
        self.role = role
        self.msgstring=msgstring

""""Creating a class for the model"""
class Gem_Bookish:
    def __init__(self,model_name = "gemini-1.5-pro-latest",generation_config=generation_config,system_instruction=system_instruction,safety_settings=safety_settings):
        self.model = model_name
        self.generation_config = generation_config
        self.system_instruction = system_instruction
        self.safety_settings = safety_settings  

        self.model = genai.GenerativeModel(model_name=self.model,
                              generation_config=self.generation_config,
                              system_instruction=self.system_instruction,
                              safety_settings=self.safety_settings)
        self.messages: list[MessageContent] = []
        self.convo = None
    """This fucntion receives prompt/question from the user"""
    def chat_gemini(self, prompt:str):
            self.convo = self.model.start_chat()
            self.convo.send_message(prompt)
            
            self.add_message(MessageContent( role ="user",msgstring=prompt))
    """This function receives response from gemini"""
    def get_answer(self)->MessageContent:
        """Decoding the location of the response given by gemini"""
        response = self.convo.history[1].parts[0].text
        """To check out the response given by gemini in terminal"""
        print("Response: ", response)
        answer = (MessageContent( role ="model",msgstring=response))
        self.add_message(answer)
        return answer.msgstring
    """This function appends the user questions and model responses to a list to be displayed on the user interface"""
    def add_message(self,message)->None:
            self.messages.append(message)

    """This function returns the list of messages"""         
    def get_message_history(self)->list[MessageContent]:
            return self.messages
        
