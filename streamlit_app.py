from datetime import date, timedelta, datetime
import streamlit as st
from streamlit_timeline import st_timeline
import pandas as pd


st.set_page_config(layout="wide")
st.title("Timeline")
today = datetime.now().strftime('%Y-%m-%d')
today_90d = (datetime.now() + timedelta(days=90) ).strftime('%Y-%m-%d')

items = [
    {"content": "First Event", "start": today},
    {"content": "Last Event", "start": today_90d}]

df = pd.DataFrame(items)

edited_df = st.experimental_data_editor(df, num_rows="dynamic")
timeline = st_timeline(edited_df.to_dict("records"), groups=[], options={}, height="300px")
# st.subheader("Selected item")
# st.write(timeline)
