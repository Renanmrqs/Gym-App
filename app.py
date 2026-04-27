import requests
from api import BASE_URL, get
import streamlit as st


def sidebar():
    with st.sidebar:
        try:
            api_info = requests.get(f"{BASE_URL}/health", timeout=3)
            st.success("🟢 API Online")
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            st.error('🔴 API Offline')
        except requests.exceptions.HTTPError:
            st.warning('🟡 API Online, but with errors')

sidebar()


def login(user, password):
    form_data = {'username': user, 'password': password}
    response = requests.post(f'{BASE_URL}/login', data=form_data)
    return response

st.title('Gym Register', text_alignment='center')
st.subheader('Login', text_alignment='center')
username = st.text_input('Username: ')
password = st.text_input('Password: ', type='password')

if st.button('Login'):
    log_info = login(username, password)
    if log_info.status_code == 200:
        user_logged = log_info.json()
        token = user_logged['access_token']
        
        st.session_state['user_token'] = token
        st.success(f'{username} logged!')
    else:
        msg_error = log_info.json()
        st.error(f'Error : {msg_error['detail']}')
st.warning(f'If not registred, click on button {st.button('Register')}')        
