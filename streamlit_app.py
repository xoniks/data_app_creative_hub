import pandas as pd
import streamlit as st

df = None

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:    
    df = pd.read_csv(uploaded_file)
    st.write('File uploaded')
    list_of_countries = df['country'].unique()
    country_value_counts = df['country'].value_counts()
    count_country_dict = country_value_counts.to_dict()
  


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
    # num = len(df[df['country']==option])
    num = count_country_dict[option]
    st.write(f'Your {option} occurs {num} times')
