import requests
import api
import streamlit as st
from app import sidebar
import pandas as pd
import datetime as dt
import plotly.express as px

st.title('History Page')

try:
    if 'user_token' in st.session_state:
        head = {'Authorization': f'Bearer {st.session_state["user_token"]}'}
    

        def users():
            user_api = api.get("/users", head)
            last = []
            for item in user_api:
                last.append(f'{item['id']} - {item['name']}')
            return last 

        user = st.session_state.get('user_name')
        try:
            h = api.get(f"/history/{user}", head)
            df = pd.DataFrame(h)
            df['datetime'] = pd.to_datetime(df['datetime'], format='ISO8601')
            df['datetime'] = df['datetime'].dt.tz_convert('America/Sao_Paulo')
            df['datetime'] = df['datetime'].dt.strftime('%d/%m/%Y %H:%M')
            st.subheader(f"{user}'s History")
            st.dataframe(df)
            
            select_exercise = st.selectbox("Select exercise to see your evolution", df['exercise'].unique())
            
            if st.button('Filter'):
                df_filtered = df[df['exercise'] == select_exercise]
                df_max = df_filtered.groupby(['exercise', 'datetime'])['weight'].max().reset_index()
                
                fig = px.line(df_max, x='datetime', y='weight', color='exercise')
                fig.update_yaxes(dtick=5)
                st.plotly_chart(fig)
            
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
                    h = api.get(f"/history/{compare_name[1].strip()}", head)
                    df = pd.DataFrame(h)
                    df['datetime'] = pd.to_datetime(df['datetime'])
                    df['datetime'] = df['datetime'].dt.tz_convert('America/Sao_Paulo')
                    df['datetime'] = df['datetime'].dt.strftime('%d/%m/%Y %H:%M')
                    if compare_name[1].strip() == user:
                        raise NameError
                    st.subheader(f'{compare_name[1]} History')
                    st.dataframe(df)
                except requests.exceptions.HTTPError:
                    st.error(f"{compare_name[1]} hasn't logged any workouts yet")
                except NameError:
                    st.error('You already seen you history')
        sidebar()
    else:
        st.warning('Please, loggin for see this page')
except requests.exceptions.HTTPError:
    st.warning('Please, loggin for see this page')
        
        

