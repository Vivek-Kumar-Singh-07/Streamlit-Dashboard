import streamlit as st
import pandas as pd

# Sidebar title 
st.sidebar.title('DASHBOARD')

# Theme
st.title("""LET'S GET STARTED""")

#Columns

col1, col2, col3,col4 = st.columns(4)

with col1:
    st.subheader('KPI-1')
    st.success('Coming Soon!')

with col2:
    st.subheader('KPI-2')
    st.success('Coming Soon!')

with col3:
    st.subheader('KPI-3')
    st.success('Coming Soon!')

with col4:
    st.subheader('KPI-4')
    st.success('Coming Soon!')


st.divider()

#file uploader

upload_file = st.file_uploader("Upload a CSV file:", type='csv')

if upload_file is not None:
    file = pd.read_csv(upload_file) 
    st.write(file.head(20))

# Column names as filter

if upload_file is not None:
    column_filter = st.sidebar.selectbox("Filter-1 (X-Axis)", list(file.columns))
    column_filter1 = st.sidebar.selectbox("Filter-2 (Y-Axis)", list(file.columns))
else:
    st.sidebar.error('Upload your file to see Column Names as Filter')

if upload_file is not None:
    st.subheader(f"Line chart based on {column_filter} and {column_filter1}")
    st.line_chart(data=file,x=column_filter, y=column_filter1)



