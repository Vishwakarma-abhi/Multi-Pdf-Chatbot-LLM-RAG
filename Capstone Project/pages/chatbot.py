import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from streamlit_chat import message as st_message

load_dotenv()

@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

@st.cache_data
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks):
    embeddings = load_embeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

@st.cache_resource
def get_conversational_chain():
    prompt_template = """
    You are an intelligent assistant trained to provide accurate and concise answers based on the provided context.
    Analyze the given context thoroughly and generate a clear response to the user's inquiry. 
    If the answer is not found within the context, respond with "The information is not available in the provided context." 
    
    "Ensure that the output only includes the answer without any mention of the context or the question."

    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    """

    llm = HuggingFacePipeline.from_model_id(
        model_id="model/Phi-3-mini-4k-instruct",
        task="text-generation",
        pipeline_kwargs={"max_new_tokens": 100, "pad_token_id": 50256, "temperature": 0.1},
    )

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(llm, chain_type="stuff", prompt=prompt)

def user_input(user_question):
    embeddings = load_embeddings()
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()
    st_message("Assistant is thinking...", is_user=False)
    response = chain.invoke(
        {"input_documents": docs, "question": user_question}, return_only_outputs=True
    )
    final_output = response["output_text"].split("Answer:")[-1].strip()
    st_message(final_output, is_user=False)

def main():
    st.set_page_config(page_title="Chat with PDF using Phi-mini-4k-instruct")
    st.header("Chat with PDF using Phi-mini-4k-instruct Model")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "processing_complete" not in st.session_state:
        st.session_state.processing_complete = False

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Processing complete!")
                st.session_state.processing_complete = True

    if st.session_state.processing_complete:
        user_question = st.text_input("Ask a Question from the PDF Files", key="input")
        if st.button("Send") and user_question:
            st_message(user_question, is_user=True)
            user_input(user_question)

    for message in st.session_state.messages:
        st_message(message["content"], is_user=(message["role"] == "user"))

main()
