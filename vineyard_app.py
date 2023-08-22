import streamlit as st
from predict_page import show_pred
from dashboard import show_dashboard
from PIL import Image

# Load and resize the logo
image_path = "DTA Logo.png"
logo = Image.open(image_path)
new_size = (150, 100)
logo = logo.resize(new_size)

# Define valid credentials
valid_username = "jay"
valid_password = "DTA"

# Check if user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Store the selected page globally
selected_page = None

def show_sidebar():
    global selected_page  # Use the global selected_page variable
    selected_page = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))
    show_sidebar_image()

def show_pages():
    if selected_page == "Explore":
        show_dashboard()
    elif selected_page == "Predict":
        show_pred()

def show_image():
    st.markdown("<br>" * 4, unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        st.image(logo, use_column_width=False, width=new_size[0])

def show_sidebar_image():
    st.sidebar.markdown("<br>" * 12, unsafe_allow_html=True)
    st.sidebar.image(logo, use_column_width=False, width=new_size[0])

# Placeholder for content
content_placeholder = st.empty()

if not st.session_state.logged_in:
    st.title('🍇 Vineyard Sign in')
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if username == valid_username and password == valid_password:
            st.session_state.logged_in = True
            # Clear the content placeholder after successful login
            content_placeholder.empty()
        else:
            st.error("Invalid credentials")
    show_image()

if st.session_state.logged_in:
    show_sidebar()
    show_pages()

