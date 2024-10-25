import streamlit as st

import streamlit as st
import hashlib
from pymongo import MongoClient

# MongoDB connection
# client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB connection string
# db = client['auth_db']  # Database name
# collection = db['users']  # Collection name

client = MongoClient("mongodb+srv://rashmi0011:jjAIzqce0wdaaBAO@cluster0.aqc7o.mongodb.net/")

# Access a database


db = client['Database1']

# Access a collection
collection = db['Collection1']


# import streamlit as st
# import hashlib
# from pymongo import MongoClient

# # MongoDB connection
# client = MongoClient('mongodb://localhost:27017/')  # Update with your MongoDB connection string
# db = client['auth_db']  # Database name
# collection = db['users']  # Collection name

# Hash function for password security
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Login function to authenticate user
def login(email, password):
    hashed_pw = hash_password(password)
    user = collection.find_one({"email": email, "password": hashed_pw})
    return user

# Main application logic
st.title("User Authentication")

# Login Form
def login_page():
    st.header("Login Page")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = login(email, password)
        if user:
            st.session_state.username = name
            st.session_state.password = password
            st.session_state.email = email
            collection.find_one()
            st.balloons()
            st.success(f"Welcome back! You are logged in.")
            #st.switch_page(r"pages\profile.py")
        else:
            st.warning("Invalid email or password")

    # Link to Signup Page
    st.write("Don't have an account?")
    if st.button("Sign Up Now"):
        st.switch_page(r"pages\signup.py")
    # def login():
#     st.write("....")
# login()
if ('username' not in st.session_state) and ('password' not in st.session_state):
    login_page()
    print("Session state" , st.session_state)
else:
    st.toast("**:red[You are already logged in]**")