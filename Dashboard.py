import streamlit as st

#Title in the sidebar
st.sidebar.title('SALES DASHBOARD')

#Filters
region_filter=st.sidebar.selectbox("Region",['All','Americas','EMEAR','APJC'])
segment_filter=st.sidebar.selectbox("Segment",['All','Enterprise','Mid-Market','SMB'])


# Columns

col1, col2, col3,col4 = st.columns(4)

with col1:
    st.subheader('Sales')
    # st.success('$2.5M')
    if region_filter == 'Americas':
        print(st.success('$2.5M'))
    elif region_filter=='APJC':
        print(st.success('$2.8M'))
    else:
        print(st.success('$3M'))

with col2:
    st.subheader('Profit')
    st.success('$1M')

with col3:
    st.subheader('Partners')
    st.success('2500')

with col4:
    st.subheader('Customer')
    st.success('1.1M')