import pandas as pd
import streamlit as st

df = pd.read_csv('sample_data.csv')

list_of_countries = df['country'].unique()

if st.button('Show list of countries'):
    st.write(list_of_countries)