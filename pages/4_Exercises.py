import requests
import api
import streamlit as st


def exercises_post(name):
    api.post("/exercises", name)

st.title('Exercises Page')


st.subheader('Create Exercise')
name = st.text_input('Type exercise: ')

if st.button('Create'):
    try:
        (exercises_post({'name': name}))
        st.success(f'Exercise {name} Created')
    except requests.HTTPError:
        st.error(f'Exercise {name} is cadastred yet')


st.subheader('Exercises on table')
st.dataframe(
    api.get("/exercises")
    )

