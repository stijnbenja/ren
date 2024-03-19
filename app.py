import functions
import streamlit as st
st.title('🏃🏼‍♂️ Running converter')

tabs = st.tabs(['Tempo to km/h', 'Km/h to tempo', 'Target to speed'])



with tabs[0]:
    st.subheader('Tempo to km/h')
    with st.container(border=True):
        minutes = st.number_input('minutes',min_value=0, max_value=60, step=1, value=6)
        seconds = st.number_input('seconds',min_value=0, max_value=60, step=1)
        
        st.subheader(f'{functions.tempo_to_kmh(minutes=minutes, seconds=seconds)} km/h')
        

with tabs[1]:
    st.subheader('Km/h to tempo')
    with st.container(border=True):
        kmh = st.number_input('km/h',min_value=0.0, value=10.0,max_value=60.0, step=0.1)
        
        tempo = functions.kmh_to_tempo(kmh)
        
        st.subheader(f'{tempo[0]}m {tempo[1]}s')
        
        
        
    
    
with tabs[2]:
    st.subheader('Target to speed')
    with st.container(border=True):
        km = st.number_input('km',min_value=0.0, step=0.01, value=5)
        target_minutes = st.number_input('minutes',key=2,min_value=0, step=1, value=30)
        
        speed = functions.target_to_speed(km=km,minutes=target_minutes)
        
        st.subheader(f"{speed['tempo'][0]}m {speed['tempo'][1]}s")
        st.subheader(f"{speed['kmh']} km/h")
        
        
        
        
    
    