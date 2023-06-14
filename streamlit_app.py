import pandas as pd
import streamlit as st

df = None

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write('File uploaded')
  list_of_countries = df['country'].unique()
  


# if st.button('Show list of countries'):
#     if df is None:
#         st.write('Upload the dataframe')
#     else:
#         list_of_countries = df['country'].unique()
        # st.write(list_of_countries)
        
option = st.selectbox(
    'Choose your country:',
    list_of_countries)

if st.button("Show how many times you country occurs in dataframe"):
    num = len(df[df['country']==option])
    st.write(f'Your {option} occurs {num} times')
