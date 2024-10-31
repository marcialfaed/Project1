import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def contact_page():
    st.title("Contact Us")
    st.write("📞 Reach us at: **+639553210900**")
    st.write("For any questions, feel free to send us a message below!")

    name = st.text_input("Your Name", placeholder="Enter your name here")
    email = st.text_input("Your Email", placeholder="Enter your email here")
    message = st.text_area("Your Message", placeholder="Type your message here...")

    if st.button("Send"):
        if name and email and message:
            st.success("Your message has been sent successfully!")
            sender_email = "your_email@gmail.com"
            sender_password = "your_password"  # App password
            recipient_email = "your_email@gmail.com"

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = f"New Contact Form Message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            msg.attach(MIMEText(body, 'plain'))

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                server.quit()
                st.success("Your message was emailed successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please fill in all fields before sending.")
