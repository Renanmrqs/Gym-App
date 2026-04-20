import requests
import api
import streamlit as st

if 'user_token' in st.session_state:
    head = {'Authorization': f'Bearer {st.session_state["user_token"]}'}
    
    st.title('Register Training')
    st.subheader('Register your workout')

    # funcoec chamando a api
    ##
    def users():
        users_api = api.get("/users")
        last = []
        for item in users_api:
            last.append(f'{item['id']} - {item['name']}')
        return last

    

    def exercises():
        exercises_api = api.get("/exercises")
        print(exercises_api)
        last = []
        for item in exercises_api:
            last.append(f'{item['id']} - {item['name']}')
        return last 
    
    print(exercises())
    ##
    ## primeiro selectbox registrando treino e horario do usuario

    select_id = st.selectbox(
        "Select your ID",
        users()
    )


    if 'id_workout' not in st.session_state:
        st.session_state.id_workout = None

    if st.button("Submit id"):   
        id = select_id.split('-')[0]
        sucess = api.post(f'/workout', {'id_user': id}, head)
        st.session_state.id_workout = sucess['id']
        st.success(sucess['message'])

    ##
    ## selectbox do usuario escolher o exercicio para registrar

    if 'id_workout_exercise' not in st.session_state:
        st.session_state.id_workout_exercise = None

    if st.session_state.id_workout is not None:
        select_exercise = st.selectbox(
            "Select exercise for registrer",
            exercises()
        )

        if st.button("Choise exercise"):
            id_exercise = select_exercise.split(' - ')[0]
            st.session_state.id_exercise = id_exercise
            succes_exercise = api.post(f'/workout_exercise', {'id_workout': st.session_state.id_workout, 'id_exercise': st.session_state.id_exercise}, head)
            st.session_state.id_workout_exercise = succes_exercise['id']
            st.success(succes_exercise['message'])
            
    ##
    ## selectbox do usuario escolher as sets

    if st.session_state.id_workout_exercise is not None:
        if 'set' not in st.session_state:
            st.session_state.set = 0
        select_sets = st.selectbox("Choice a quantity sets for registrer",
        (1, 2, 3, 4))
        
        if st.button('Change sets'):
            st.session_state.set = select_sets
        
        sets = 1
        
        if st.session_state.set > 0:
            st.write(f'Remaining Sets: {st.session_state.set}')
            
            weight = st.number_input(f'Insert weight for {sets} set', min_value=1, icon='💪', key='weight')
            
            reps = st.number_input(f'Insert quantity of reps for {sets} set', min_value=1, max_value=30, key='reps') 
            sets += 1
            if st.button('Submit set'):
                sucess_sets = api.post(f'/sets', {'weight': weight, 'reps': reps, 'id_workout_exercise': st.session_state.id_workout_exercise}, head)
                st.success(sucess_sets['message'])
else:
    st.warning('Please, loggin for see this page')            