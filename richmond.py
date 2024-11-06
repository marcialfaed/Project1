import streamlit as st
from menu import menu_page
from about import about_page
from contact import contact_page
from billing import billing_page

# Set wide layout
st.set_page_config(layout="wide")  # Allows full-width layouts


# Retrieve the current tab from query parameters, or default to "Home (Menu)"
tab = st.query_params.get("tab", "Home (Menu)")


# Navigation menu with query parameters
nav_options = ["Home (Menu)", "About", "Contact", "Billing Method"]
selected_tab = st.selectbox("Navigate", nav_options, index=nav_options.index(tab), key="top_nav", label_visibility="collapsed")


# Update query parameter whenever the tab is changed
st.query_params.tab = selected_tab


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
