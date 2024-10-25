import streamlit as st
import hashlib
import re
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page
client = MongoClient("mongodb+srv://rashmi0011:jjAIzqce0wdaaBAO@cluster0.aqc7o.mongodb.net/")


# Access a database


db = client['Database1']
# Access a collection
collection = db['Collection1']

# Hash function for password security
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Function to validate email format
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Signup function to store user data
def signup(name, email, password):
    if collection.find_one({"email": email}):
        return False, "Email already exists"
    else:
        hashed_pw = hash_password(password)
        collection.insert_one({"name": name, "email": email, "password": hashed_pw})

        return True, "Signup successful"
def sign():
# Main application logic
    st.title("Sign Up")

    # Signup Form
    st.header("Create an Account")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if (name == ""):
            st.warning("Enter your name")
        if not is_valid_email(email):
            st.warning("Please enter a valid email address.")
        elif len(password) < 8:
            st.warning("Password must be at least 8 characters long.")
        elif not re.search(r'\d', password) or not re.search(r'[A-Za-z]', password) or not re.search(r'\W', password):
            st.warning("Password must contain at least one alphanumeric character and one special character.")
        else:
            success, message = signup(name, email, password)
            st.session_state.username = name
            st.session_state.password = password
            st.session_state.email = email
            if('profile_created' in st.session_state):
                del st.session_state['profile_created']
            if('learning_path_generated' in st.session_state):
                del st.session_state['learning_path_generated']
            if success:
                st.success(message)
                st.balloons()
                print(st.session_state)
                st.switch_page(r"pages\interest.py")
                
            else:
                st.warning(message)

if ('username' not in st.session_state) and ('password' not in st.session_state):
    sign()
else:
    st.toast("**:red[You are already logged in]**")
