import pandas as pd
import streamlit as st

df = None

st.title('Creative hub data science project ')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) 
    st.write('File uploaded')
    
    
if df is None:
    st.write('Upload the dataframe')   
else:
    list_of_countries = df['country'].unique()
    country_value_counts = df['country'].value_counts()
    count_country_dict = country_value_counts.to_dict()
    st.bar_chart(country_value_counts)  
    st.divider()        
    max_range = df['numberrange'].max()
    mean_range = df['numberrange'].mean()
    min_range = df['numberrange'].min()
    median_range = df['numberrange'].median()

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.subheader("Max of range")
        st.write(f'Max range is {max_range}')
        
    with col2:
        st.subheader("Mean of range")
        st.write(f'Mean range is {mean_range}')

    with col3:
        st.subheader("Median range ")
        st.write(f'Median range is {median_range}')

    with col4:
        st.subheader("Min of range")
        st.write(f'Min range is {min_range}')
    st.divider()  

    option = st.selectbox("Choose a country", list_of_countries)
    
if st.button("Print country stats"):
    try:
        num = count_country_dict[option]
        st.write(f'Your {option} occurs {num} times')
        desc_country = df[df['country']==option]['numberrange'].describe()
        desc_country = pd.DataFrame(desc_country).transpose()
        st.write(desc_country)
    except:
        st.write('You didnt upload the file ')
