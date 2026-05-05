import requests
from api import BASE_URL, get
import streamlit as st
import time

def sidebar():
    with st.sidebar:
        try:
            api_info = requests.get(f"{BASE_URL}/health", timeout=3)
            st.success("🟢 API Online")
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            st.error('🔴 API Offline')
        except requests.exceptions.HTTPError:
            st.warning('🟡 API Online, but with errors')

        if 'user_token' in st.session_state:
            if st.button("Logout", type="primary", width="stretch"):
                    try:
                        head = {'Authorization': f'Bearer {st.session_state["user_token"]}'}
                        response = requests.post(f"{BASE_URL}/logout", headers=head)
                        if response:
                            st.toast("🟢 Sucessfull Logout")
                            del st.session_state['user_token']
                            del st.session_state['user_name']
                            del st.session_state['user_id']
                            time.sleep(1.5)
                            st.switch_page('pages/2_login.py')
                    except Exception as e:
                        st.error(f'Erro inesperado: {e}')

            


sidebar()




st.title(":red[_Gym Register_]", text_alignment='center')
st.subheader(':blue[Register your workouts and follow your evolution]', text_alignment='center')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.subheader("Log and save your infos on cloud ")
    st.image("img/register.png", width="stretch") 
with col2:
    st.subheader("Follow your progress and compare with other users")
    st.image("img/historic.png", width="stretch")

st.write("")
st.write("")
st.write("")

with col3:
    st.subheader("Track all register and all of your workouts")
    st.image("img/register_treine_sucessful.png", width="stretch")
with col4:
    st.subheader("Break your limits! register now")
    st.image("img/peito.png", width="stretch")
    
st.markdown("<h1 style='text-align: center; color: white;'>Get started now!</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Select on sidebar! 👈</h3>", unsafe_allow_html=True)