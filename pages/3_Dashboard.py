import requests
import api
import streamlit as st
from app import sidebar

sidebar()

if 'user_token' in st.session_state:
    head = {'Authorization': f'Bearer {st.session_state["user_token"]}'}

    user = st.session_state.get('user_name')
    try:
        historic = api.get(f"/history/{user}")

        user_id = st.session_state.get('user_id')
        exercises = api.get("/exercises")
        sets = historic
        workouts = api.get(f"/workout_detail_w_user/{user_id}")

        maximo = 0
        name_ex = "N/A"
        for i, historic in enumerate(historic):
                actual_weight = (historic["weight"])
                if actual_weight >= maximo:
                    maximo = actual_weight
                    name_ex = historic["exercise"]

        st.title('Gym Register')
        st.subheader(
            f'Welcome back to Gym Register {st.session_state.get('user_name', 'Renan')}! see your week stats.')
        st.sidebar.write('Dashboard')

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        col1.metric('Exercices Registred', len(exercises), border=True)
        col2.metric('Workouts Complete', len(workouts), border=True)

        col3.metric('Sets completes', len(sets), border=True)
        col4.metric('Max Weight', maximo, delta=name_ex, border=True)
    except requests.exceptions.HTTPError:
        st.subheader(
            f'Welcome to Gym Register {st.session_state.get('user_name', 'Renan')}! Please, add exercises to see your week stats.')
else:
    st.warning('Please, loggin for see this page')
