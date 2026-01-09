import streamlit as st

#Title in the sidebar
st.sidebar.title('SALES DASHBOARD')

#Filters
st.sidebar.selectbox("Region",['All','Americas','EMEAR','APJC'])
st.sidebar.selectbox("Segment",['All','Enterprise','Mid-Market','SMB'])


# Columns

col1, col2, col3,col4 = st.columns(4)

with col1:
    st.subheader('Sales')
    st.success('$2.5M')

with col2:
    st.subheader('Profit')
    st.success('$1M')

with col3:
    st.subheader('Partners')
    st.success('2500')

with col4:
    st.subheader('Customer')
    st.success('1.1M')