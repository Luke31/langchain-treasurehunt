from langchain.callbacks import StreamlitCallbackHandler
import streamlit as st
from actor.main import run

st.title("Treasurehunt")
ui_url = "http://127.0.0.1:8089/"
# st.write("check out this [link](%s)" % url)
st.markdown("Open the UI here: %s" % ui_url)
model = st.radio(
    "Which model do you wanna use for the problem solver agent?",
    ('gpt-4', 'gpt-3.5-turbo'))

if st.button('Start solving'):
    st.write(f'Starting to solve using model {model}...')
    st_callback = StreamlitCallbackHandler(st.container())
    response = run(st_callback, model)
    st.write(response)
