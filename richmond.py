import streamlit as st

st.title("Welcome to [Your Restaurant's Name] 🍽️")
st.header("About Us")
st.write("Welcome to [Your Restaurant]! We specialize in [Cuisine Type]. Enjoy a cozy atmosphere with delicious dishes.")

# Menu Section
st.header("Menu")
st.subheader("Appetizers")
st.write("- Dish 1: Description")
st.write("- Dish 2: Description")

st.subheader("Main Dishes")
st.write("- Dish 3: Description")
st.write("- Dish 4: Description")

st.subheader("Desserts")
st.write("- Dish 5: Description")
st.write("- Dish 6: Description")

# Hours & Location
st.header("Hours & Location")
st.write("Monday - Friday: 9 AM - 10 PM")
st.write("Saturday - Sunday: 11 AM - 11 PM")
st.map()  # Optionally add a map or location

# Optional Contact Form
st.header("Contact Us")
st.text_input("Name")
st.text_area("Message")
st.button("Send")
