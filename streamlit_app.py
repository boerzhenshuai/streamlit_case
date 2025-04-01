# -*- coding: utf-8 -*-
# @Time : 2025/4/1 8:14
# @Author : boer
# @File : streamlit_app.py
# @Software: PyCharm
import streamlit as st
from openai import OpenAI
st.title("Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"]=[{"role":"assistant","content":"How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    client = OpenAI(api_key="sk-c4b8c501c53843909356cb43e3e42797", base_url="https://api.deepseek.com")
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    response=client.chat.completions.create(model="deepseek-chat",
        messages=st.session_state.messages)
    msg=response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
