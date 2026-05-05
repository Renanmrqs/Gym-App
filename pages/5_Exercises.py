import requests
import api
import streamlit as st
from app import sidebar

sidebar()

try:
    if 'user_token' in st.session_state:
        def exercises_post(name, head):
            api.post("/exercises", name, head)

        head = {'Authorization': f'Bearer {st.session_state["user_token"]}'}

        
        st.title('Exercises Page')


        st.subheader('Create Exercise')
        name = st.text_input('Type exercise: ')

        if st.button('Create'):
            try:
                (exercises_post({'name': name}, head))
                st.success(f'Exercise {name} Created')
            except requests.exceptions.HTTPError as e:
                st.error(f'Error: {e.response.json()['detail']}')


        st.subheader('Exercises on table')
        st.dataframe(
            api.get("/exercises", head)
            )
    else:
        st.warning('Please, loggin for see this page')            
except requests.exceptions.HTTPError:
    st.warning('Please, loggin for see this page')