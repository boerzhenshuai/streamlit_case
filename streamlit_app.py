# -*- coding: utf-8 -*-
# @Time : 2025/4/1 8:14
# @Author : boer
# @File : streamlit_app.py
# @Software: PyCharm
import streamlit as st
name=st.text_input("input your name:")
age=st.slider("input your age",0,100)
st.write(f'你好，{name}!你的年龄{age}')