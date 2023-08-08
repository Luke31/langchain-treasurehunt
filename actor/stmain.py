import streamlit as st
from actor.main import run

st.title("Treasurehunt")
model = st.radio(
    "Which model do you wanna use for the problem solver agent?",
    ('gpt-4', 'gpt-3.5-turbo'))

if st.button('Start solving'):
    st.write('Starting to solve...')
    # TODO: Redirect console output
    run()

