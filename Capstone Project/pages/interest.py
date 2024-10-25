from pymongo import MongoClient, ReturnDocument
import streamlit as st

client = MongoClient("mongodb+srv://rashmi0011:jjAIzqce0wdaaBAO@cluster0.aqc7o.mongodb.net/")
db = client['Database1']
collection = db['Collection1']

# def show_learning_path():
#         st.title("Your Learning Path")

#         if st.session_state.learning_path_generated:
#             st.write("### Learning Path for:", st.session_state.selected_skill)
#             st.write("**Current Knowledge:**", ", ".join(st.session_state.current_knowledge))
#             st.write("**Learning Level:**", st.session_state.learning_level)
            
#             # Placeholder for displaying the uploaded files
#             st.write("**Uploaded Files:**")
#             for file in st.session_state.uploaded_files:
#                 st.write(file.name)
            
#             # Placeholder for generated learning path content
#             st.write("Your learning path will be generated based on the uploaded knowledge base.")

def create_profile():
     # Function to upload knowledge base
    # def upload_knowledge_base():
    #     st.title("Upload Your Knowledge Base")

    #     # Knowledge Base Upload
    #     st.subheader("Upload Your Knowledge Base / Files")
    #     uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    #     # Level Selection
    #     st.subheader("Select Level for Learning Path")
    #     learning_level = st.selectbox("Choose your learning level:", ["Beginner", "Intermediate", "Advanced"])

    #     # Generate Learning Path button
    #     if st.button("Generate Learning Path"):
    #         if uploaded_files:
    #             st.session_state.uploaded_files = uploaded_files
    #             st.session_state.learning_level = learning_level
    #             st.session_state.learning_path_generated = True
    #             st.success("Files uploaded successfully! Generating learning path...")
    #             show_learning_path()
                
    #         else:
    #             st.warning("Please upload at least one PDF file.")

    def create_user_profile():
        st.title(f"Welcome {st.session_state['username']} 😎")
        st.header("Create Your User Profile")

        # Current Knowledge
        st.subheader("Select Your Current Knowledge")
        current_knowledge = st.multiselect(
            "Choose your current skills:",
            ["Java", "Python", "Machine Learning", ".Net", "Flutter", "React"]
        )

        # Learning Path Selection
        st.subheader("What do you want to learn?")
        learning_options = ["Select Skill","Java", "Python", "Machine Learning", ".Net", "Flutter", "React", "Other"]
        selected_skill = st.selectbox("Choose a skill to learn:", learning_options)

        # Input box for 'Other'
        if selected_skill == "Other":
            other_skill = st.text_input("Please specify your skill or topic:")

        # Create User Profile button
        if st.button("Create User Profile"):
            st.session_state.selected_skill = other_skill if selected_skill == "Other" else selected_skill
            st.session_state.current_knowledge = current_knowledge
            st.session_state.profile_created = True
            print(current_knowledge)
            print(type(current_knowledge))
            print(selected_skill)

            ## Add data to database
            print("Session state" , st.session_state)
            filter_query = {'name': st.session_state.username, 'email' : st.session_state.email}
            update_query = {'$set': {'current_skills': current_knowledge, "aim":selected_skill }}
            updated_document = collection.find_one_and_update(
            filter=filter_query,
            update=update_query,
            return_document=ReturnDocument.AFTER)
            st.success("User Profile Created! Redirecting to upload knowledge base...")

            if(st.button("Chat Bot")):
                st.switch_page("pages\chatbot.py")

   
    # Function to show generated learning path

    # Streamlit pages navigation
    if ("profile_created" not in st.session_state):
        create_user_profile()

    elif(st.session_state.profile_created == False):
        st.toast("Profile not found")
    else:
        if(st.button("View profile")):
            st.switch_page(r"pages\profile.py")
        # if(st.button("Update profile")):
        #     create_profile()
        if(st.button("Chat Bot")):
            st.switch_page("pages\chatbot.py")


if('username' not in st.session_state):
    st.header("**:red[You are not logged in]**")
    if(st.button("Sign Up Now")):
        st.switch_page(r"pages\signup.py")
    if(st.button("Log In")):
        st.switch_page(r"pages\login.py")
else:
    client = MongoClient("mongodb+srv://rashmi0011:jjAIzqce0wdaaBAO@cluster0.aqc7o.mongodb.net/")
    db = client['Database1']
    collection = db['Collection1']
    query = {'name': st.session_state.username, 'aim': {'$exists': True}}
    document = collection.find_one(query)
    if(document and "learning_path_generated" in st.session_state ):
        st.header("**Profile created**")
        if(st.button("View profile")):
            st.switch_page(r"pages\profile.py")
        if(st.button("Update profile")):
            create_profile()
        if(st.button("Chat Bot")):
            st.switch_page("pages\chatbot.py")
    else:
        create_profile()



