import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        col1, col2, col3 = st.columns([1, 1, 3])  # Adjust column ratios as needed
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
    st.write("📞 Reach us at: **+639553210900**")
    st.write("For any questions, feel free to send us a message below!")

    # Creating input fields
    name = st.text_input("Your Name", placeholder="Enter your name here")
    email = st.text_input("Your Email", placeholder="Enter your email here")
    message = st.text_area("Your Message", placeholder="Type your message here...")

    # Submission button
    if st.button("Send"):
        if name and email and message:
            st.success("Your message has been sent successfully!")

            # Email details
            sender_email = "marcfaedm@gmail.com"
            sender_password = "vmar uedy dzwj kobr"  # App password
            recipient_email = "marcfaedm@gmail.com"

            # Set up the MIME
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = f"New Contact Form Message from {name}"

            # Body of the email
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()  # Enable security
                server.login(sender_email, sender_password)
                server.send_message(msg)
                server.quit()
                st.success("Your message was emailed successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
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

