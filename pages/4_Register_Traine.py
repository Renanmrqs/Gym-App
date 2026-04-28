import requests
import api
import streamlit as st
from app import sidebar

sidebar()

if 'user_token' in st.session_state:
    head = {'Authorization': f'Bearer {st.session_state["user_token"]}'}
    id_user = st.session_state.user_id
    
    st.title('Register Training')
    st.subheader('Register your workout')

    

    def exercises():
        exercises_api = api.get("/exercises")
        last = []
        for item in exercises_api:
            last.append(f'{item['id']} - {item['name']}')
        return last 
    



    if 'id_workout' not in st.session_state:
        if st.button('register new day of training', type='primary'):
            response = api.post(f'/workout', {'id_user': int(id_user)}, head)
            st.session_state.id_workout = response['data']['id']
            st.rerun()

    
    if 'id_workout' in st.session_state:    
        select_exercise = st.selectbox(
            "Select exercise for registrer",
            exercises()
        )

        if st.button("Choose exercise"):
                
                id_exercise = select_exercise.split(' - ')[0]
                st.session_state.id_exercise = id_exercise

                succes_exercise = api.post(f'/workout_exercise', {'id_workout': st.session_state.id_workout, 'id_exercise': int(st.session_state.id_exercise)
                }, 
                head)

                
                
                
                st.success(succes_exercise['message'])
                st.session_state.id_workout_exercise = succes_exercise['data']['id']
                st.rerun()    
            
    ##
    ## selectbox do usuario escolher as sets
    
    if 'id_workout_exercise' in st.session_state:
        if 'set' not in st.session_state:
            st.session_state.set = 0
        if 'actual_set' not in st.session_state:
            st.session_state.actual_set = 0
        
        if st.session_state.set == 0:
            select_sets = st.selectbox("Choice a quantity sets for registrer",
            (1, 2, 3, 4))
            if st.button('Start sets', type='primary'):
                st.session_state.set = select_sets
                st.rerun()
        
        

        if st.session_state.set > 0:
            st.write(f'Set: {st.session_state.actual_set + 1} of {st.session_state.set}')
            
            weight = st.number_input(f'Insert weight for {st.session_state.actual_set} set', min_value=1, icon='💪', key=f'weight_{st.session_state.actual_set + 1}')
            reps = st.number_input(f'Insert quantity of reps for {st.session_state.actual_set + 1} set', min_value=1, max_value=30, key=f'reps_{st.session_state.set}') 
            
            if st.button('Submit set'):
                sucess_sets = api.post(f'/sets', {'weight': weight, 'reps': reps, 'id_workout_exercise': st.session_state.id_workout_exercise}, head)
                st.success(sucess_sets['message'])
                
                st.session_state.actual_set += 1
                
                if st.session_state.actual_set == st.session_state.set:
                    del st.session_state['id_workout_exercise']
                    del st.session_state['set']
                    del st.session_state['actual_set']
                    st.success('All sets completed!')
                    st.rerun()
                else:
                    st.rerun()
else:
    st.warning('Please, loggin for see this page')            