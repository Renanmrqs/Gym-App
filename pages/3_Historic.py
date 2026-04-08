import requests
import api
import streamlit as st


st.title('Historic Page')

st.subheader('View your historic and see your evolution')
name = st.text_input('Type your name: ')

if st.button('Search'):
    try:
        h = api.get(f"/history/{name}")
        st.subheader(f'{name} Historic')
        st.dataframe(h)
    except requests.exceptions.HTTPError:
        st.error(f'{name} not found')
        
        
# if name in sets:
#     ...

