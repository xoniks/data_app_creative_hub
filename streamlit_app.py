import pandas as pd
import streamlit as st

# df = None

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write('File uploaded')
#   st.write(df)
  
# df = pd.read_csv('sample_data.csv')



if st.button('Show list of countries'):
    if df is None:
        st.write('Upload the dataframe')
    else:
        list_of_countries = df['country'].unique()
        st.write(list_of_countries)