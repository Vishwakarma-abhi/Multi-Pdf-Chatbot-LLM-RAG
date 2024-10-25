import streamlit as st
from streamlit_extras.switch_page_button import switch_page
def Home():
# st.title("AI Powered 🤖 Personalised Learning App ")
    st.markdown("""
        <style>
            .welcome {
                animation: fadeIn 3s;
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
        <h1 class="welcome">AI Powered 🤖 Personalised Learning App!</h1>
    """, unsafe_allow_html=True)

    import time
    import streamlit.components.v1 as components

    # Lottie Animation for Celebration
    lottie_animation = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bodymovin/5.7.6/lottie.min.js"></script>
    <div id="lottie"></div>
    <script>
        var animation = bodymovin.loadAnimation({
            container: document.getElementById('lottie'),
            renderer: 'svg',
            loop: true,
            autoplay: true,
            path: 'https://assets5.lottiefiles.com/packages/lf20_hxchm3gk.json' // Celebration animation
        });
    </script>
    """


    st.write(
        "Our application leverages Generative AI to create personalized learning paths, "
        "helping you efficiently acquire new skills."
    )

    # Key Features section
    st.header("Features")
    features = [
        "🚀 **Knowledge Management**: Access technical PDFs, articles, and books.",
        "🛤️ **Personalized Paths**: Tailor your learning journey based on goals and interests.",
        "❓ **Interactive Q&A**: Ask questions and get relevant answers.",
        "🎯 **Content Recommendations**: Receive targeted suggestions."
    ]

    for feature in features:
        st.write(feature)

    # Why Choose Us section
    st.header("Why Choose Us?")
    st.write("⏳ **Efficiency**: Save time with tailored content.")
    st.write("📚 **Relevance**: Focus on what matters to you.")
    st.write("💪 **Empowerment**: Take control of your learning.")

    # Call to Action
    st.header("Get Started!")
    if st.button("Sign Up Now!"):
        st.switch_page(r"pages\signup.py")
    

Home()