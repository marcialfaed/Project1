import streamlit as st
from menu import menu_page
from about import about_page
from contact import contact_page
from billing import billing_page

# Create a top navigation bar at the top-right position
st.set_page_config(layout="wide")  # To allow full-width layouts

# Navigation menu at the top
nav_options = ["Home (Menu)", "About", "Contact", "Billing Method"]
selected_tab = st.selectbox("Navigate", nav_options, index=0, key="top_nav", label_visibility="collapsed")

# Display the selected page content
if selected_tab == "Home (Menu)":
    st.title("Welcome to Rosto Vodka!")
    menu_page()  # Display menu content by default
elif selected_tab == "About":
    about_page()
elif selected_tab == "Contact":
    contact_page()
elif selected_tab == "Billing Method":
    billing_page()
