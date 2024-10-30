import streamlit as st

# Sidebar for navigation
st.sidebar.title("Rosto vodka restaurant")
tab = st.sidebar.radio("Select a tab", ["Menu", "About", "Contact", "Billing Method"])

if tab == "Menu":
    menu_items = [
        {"name": "Adobo", "price": "$11,410.00", "image": "https://i.ibb.co/Pt0GVMM/adobo.jpg"},
        {"name": "Sinigang", "price": "$1,200,000.00", "image": "https://i.ibb.co/SyF3H94/bicol.jpg"},
        {"name": "Bicol Express", "price": "$150,000.00", "image": "https://i.ibb.co/4gkwL7d/sinigang.jpg"},
    ]
    st.title("Menu")
    for item in menu_items:
        col1, col2, col3 = st.columns([1, 3, 1])  # Adjust column ratios as needed
        with col1:
            st.image(item["image"], width=100)
        with col2:
            st.write(f"**{item['name']}**")
        with col3:
            st.write(f"Price: {item['price']}")

elif tab == "About":
    st.title("About Us")
    st.write("""
    Welcome to rosto vodka!

    At rosto vodka, we are dedicated to bringing you the authentic flavors of Filipino cuisine. Established in 2008, our restaurant has been serving the local community with passion and pride.

    Founded by ericus, our journey began with a love for cooking and sharing food with others

    Join us for a delightful dining experience that celebrates [cuisine or culture] in every bite!

    """)

elif tab == "Contact":


    st.title("Contact Us")
    
    # Display phone number
    st.write("You can reach us at: **+123456789**")
    
    # Chat box for customer messages
    st.write("If you have any questions, feel free to send us a message!")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    # Submit button
    if st.button("Send"):
        if name and email and message:
            st.success("Your message has been sent!")
            # Here you can add functionality to send the message to your email or database
        else:
            st.error("Please fill in all fields before sending.")

elif tab == "Billing Method":
    st.title("Billing Method")

    # Instructions
    st.write("Please select your preferred billing method:")

    # Payment method options
    payment_methods = ["Credit Card", "Debit Card", "PayPal", "Cash"]
    selected_method = st.selectbox("Choose a payment method", payment_methods)

    st.write(f"You selected: **{selected_method}**")

    # If using Credit or Debit Card, ask for additional details
    if selected_method in ["Credit Card", "Debit Card"]:
        st.subheader("Enter your card details:")
        card_number = st.text_input("Card Number", type="password")
        expiration_date = st.text_input("Expiration Date (MM/YY)")
        cvv = st.text_input("CVV", type="password")

        if st.button("Submit Payment"):
            if card_number and expiration_date and cvv:
                st.success("Your payment has been processed!")
            else:
                st.error("Please fill in all card details.")

    # For PayPal or Cash, provide instructions
    elif selected_method == "PayPal":
        st.write("You will be redirected to PayPal to complete your payment.")
    
    elif selected_method == "Cash":
        st.write("Please have the exact cash ready when you arrive.")

