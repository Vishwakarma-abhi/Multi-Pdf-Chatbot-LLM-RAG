import streamlit as st

if ('username' not in st.session_state) and ('password' not in st.session_state):
    st.header("**:red[You are not logged in]**")
else:
    del st.session_state['username']
    del st.session_state['password']
    del st.session_state['email']
    st.toast("**You are logged out**")
    if(st.button("Go to Home")):
        st.switch_page(r"pages\Home.py")