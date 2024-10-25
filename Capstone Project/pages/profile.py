from pymongo import MongoClient
import streamlit as st

client = MongoClient("mongodb+srv://rashmi0011:jjAIzqce0wdaaBAO@cluster0.aqc7o.mongodb.net/")
db = client['Database1']
collection = db['Collection1']

def show_profile():
    st.title(f"Welcome {st.session_state.username} 🌟 ")
    query = {'name': st.session_state.username, 'aim': {'$exists': True}}
    document = collection.find_one(query)
    if(document):
        query_two = {'name': st.session_state.username}
        projection = {'aim': 1, 'current_skills': 1}
        res = collection.find(query_two,projection)
        if res:
            for doc in res:
                aim = doc['aim']
                current_skills = doc['current_skills']
            tab1, tab2, tab3 = st.tabs(["Your Current skill set", "Your Goals","Learning Plan"])

            with tab1:
                for elem in current_skills:
                    st.markdown(elem)
            with tab2:
                st.markdown(aim)
            with tab3:
                st.markdown("Your learing plan will appear here")
            st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 1.5rem;
        font-size : 1.2rem
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.1rem;
    }
	.stTabs [data-baseweb="tab"] {
		height: 50px;
        # white-space: pre-wrap;
		# background-color: #F0F2F6;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
    }
                        

</style>""", unsafe_allow_html=True)

        else:
            st.write("No additional profile information found.")
    else:
        st.subheader("**You are have not made your profile yet**")
        if(st.button("Create profile Now")):
            st.switch_page(r"pages\interest.py")


if('username' not in st.session_state):
    st.header("**:red[You are not logged in]**")
    if(st.button("Sign Up Now")):
        st.switch_page(r"pages\signup.py")
    if(st.button("Log In")):
        st.switch_page(r"pages\login.py")
else:
    show_profile()