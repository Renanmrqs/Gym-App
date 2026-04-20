import requests
from api import BASE_URL
import streamlit as st

def login(user, password):
    form_data = {'username': user, 'password': password}
    response = requests.post(f'{BASE_URL}/login', data=form_data)
    return response

st.title('Gym Register', text_alignment='center')
st.subheader('Login', text_alignment='center')
username = st.text_input('Username: ')
password = st.text_input('Password: ', type='password')

if st.button('Login'):
    if username == '' or password == '':
        st.error('Please, fill the text fields.')
        st.stop()
    log_info = login(username, password)
    if log_info.status_code == 200:
        user_logged = log_info.json()
        token = user_logged['access_token']
        if 'user_name' not in st.session_state:
            st.session_state.user_name = username
        if 'user_id' not in st.session_state:
            st.session_state.user_id = user_logged['user_id']
        st.session_state['user_token'] = token
        st.success(f'{username} logged!')
    else:
        msg_error = log_info.json()
        st.error(f'Error : {msg_error['detail']}')
st.warning(f'If not registred, click on button:')        
if st.button('Register'):
    st.switch_page('pages/1_Register_User.py')