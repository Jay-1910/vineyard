import streamlit as st
from predict_page import show_pred
from dashboard import show_dashboard

valid_username = "jay"
valid_password = "DTA"

# Initialize a flag to keep track of whether the user is logged in
logged_in = False

if not logged_in:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if username == valid_username and password == valid_password:
        logged_in = True

        # Clear the input elements from the page after successful login
        st.empty()
        
# If the user is logged in, show the appropriate content
if logged_in:
    page = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))

    if page == "Explore":
        show_dashboard()
    else:
        show_pred()

# If the user is not logged in and has entered invalid credentials, show an error message
if not logged_in and (username != "" or password != ""):
    st.error("Invalid credentials")








