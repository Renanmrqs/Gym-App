import requests
import api
import streamlit as st
from app import sidebar

sidebar()
st.title('History Page')

def users():
    user_api = api.get("/users")
    last = []
    for item in user_api:
        last.append(f'{item['id']} - {item['name']}')
    return last 

user = st.session_state.get('user_name')
try:
    h = api.get(f"/history/{user}")
    st.subheader(f"{user}'s History")
    st.dataframe(h)
except requests.exceptions.HTTPError:
    st.error(f"{user}, you don't have a history, please log to see")

st.subheader("See another user's history")
other_name = st.selectbox(
            "Select user for search",
            users()
        )
compare_name = other_name.split('-')



if st.button('Search'):
        try:
            h = api.get(f"/history/{compare_name[1].strip()}")
            if compare_name[1].strip() == user:
                raise NameError
            st.subheader(f'{compare_name[1]} History')
            st.dataframe(h)
        except requests.exceptions.HTTPError:
            st.error(f"{compare_name[1]} hasn't logged any workouts yet")
        except NameError:
            st.error('You already seen you history')
        
        

