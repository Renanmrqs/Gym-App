import requests
import api
import streamlit as st



exercises = api.get("/exercises")
sets = api.get("/history/Renan")
workouts = api.get("/workout_detail_w_user/1")
historic = api.get("/history/Renan")


maximo = 0
name_ex = "N/A"
for i, historic in enumerate(historic):    
    actual_weight = (historic["weight"])
    if actual_weight >= maximo:
        maximo = actual_weight
        name_ex = historic["exercise"]

    



st.title('Gym Register')
st.subheader('Welcome to Gym Register Renan! see your week stats.')
st.sidebar.write('Dashboard')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

col1.metric('Exercices Registred', len(exercises), border=True)
col2.metric('Workouts Complete', len(workouts), border=True)

col3.metric('Sets completes', len(sets), border=True)
col4.metric('Max Weight', maximo, delta=name_ex,border=True)

