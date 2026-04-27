import requests
from api import BASE_URL
import streamlit as st
from app import sidebar

sidebar()

def register(user, password):
    form_data = {'name': user, 'password': password}
    response = requests.post(f'{BASE_URL}/register', json=form_data)
    return response


st.title('Gym Register', text_alignment='center')
st.subheader('Register', text_alignment='center')
username = st.text_input('Username: ')
password = st.text_input('Password: ', type='password')


if st.button('Register now'):
    if username == '' or password == '':
        st.error('Please, fill the text fields.')
        st.stop()
    with st.spinner('Wait a moment...'):
        user_log = register(username, password)
        print(user_log)
        if user_log.status_code == 200:
                reg_info = user_log.json()
                st.success('Loaded!')
                st.success(f'{reg_info["message"]} with sucess!')
                
                st.switch_page('pages/2_Login.py')
        else:
            msg_error = user_log.json()
            st.error(f'Error : {msg_error["detail"]}')

st.warning(f'If already registred, click on button:')        
if st.button('Login'):
    st.switch_page('pages/2_login.py')
