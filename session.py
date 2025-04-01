# -*- coding: utf-8 -*-
# @Time : 2025/4/1 14:47
# @Author : boer
# @File : session隔离.py
# @Software: PyCharm
import streamlit as st
def update_counter():
    st.session_state['counter']+=1

if 'counter' not in st.session_state:
    st.session_state['counter']=0

if 'my_list' not in st.session_state:
    st.session_state['my_list']=[]

st.write(f"当前计数:{st.session_state['counter']}")

st.button('增加计数',onclick=update_counter)

st.session_state['my_list'].append(st.session_state['counter'])

st.write('当前列表',st.session_state['my_list'])