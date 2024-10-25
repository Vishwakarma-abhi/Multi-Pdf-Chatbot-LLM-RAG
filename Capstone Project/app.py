import streamlit as st
# from Pages.Home import Home
# from Pages.signup import signup
about_page = st.Page(
    "Pages/Home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
login = st.Page(
    "Pages/login.py",
    title="Login",
    icon=":material/login:",
)
logout = st.Page(
    "Pages/logout.py",
    title="Logout",
    icon=":material/logout:",
)
signup = st.Page(
    "Pages/signup.py",
    title="Sign Up",
    icon=":material/login:",
)
profile = st.Page(
    "Pages/profile.py",
    title="View profile",
    icon=":material/person:",
)
after_signup = st.Page(
    "Pages/interest.py",
    title="Create profile",
    icon=":material/person_add:",
)
bot = st.Page(
    "Pages/chatbot.py",
    title="Chat",
    icon=":material/smart_toy:",
)
pg = st.navigation(
    {
        "Home": [about_page],
        "User actions": [login, signup,profile,after_signup,logout],
        "Chatbot" : [bot]
    }
)

def main():
    pg.run()
# Run the main function
if __name__ == "__main__":
    main()
