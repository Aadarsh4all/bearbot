from bardapi import Bard
import streamlit as st
from streamlit_chat import *

import os


        
 # message = input("Entre your prompt :")
 
 # print(Bard().get_answer(str(message))['content'])

st.title("BearAI......")
st.write("By Aadarsh") 

os.environ["_BARD_API_KEY"] = 'Zwgdrpi8hkvaoMEylsSyuCpTG2ygEMlayjYkG4QG5_nAqLRlTeG_2R9Npstk57EIP9ZJGQ.'

def response_api(promot) :
    message = Bard(timeout=10).get_answer(str(promot))['content']
    return message

def user_input():
    input_text = st.text_input("Enter Your Comand to Bear")
    return input_text

if 'generate' not in st.session_state:
   st.session_state['generate'] = []
if 'past' not in st.session_state:
   st.session_state['past'] = []

user_text = user_input()

if user_text :
   output = response_api(user_text)
   st.session_state.generate.append(output)
   st.session_state.past.append(user_text)


if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) -1, -1, -1):
       message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
       message(st.session_state["generate"][i], key=str(i))
      
