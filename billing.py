import streamlit as st

def billing_page():
    st.title("Billing Method")
    st.write("Please select your preferred billing method:")

    payment_methods = ["Credit Card", "Debit Card", "PayPal", "Cash"]
    selected_method = st.selectbox("Choose a payment method", payment_methods)

    st.write(f"You selected: **{selected_method}**")

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
    elif selected_method == "PayPal":
        st.write("You will be redirected to PayPal to complete your payment.")
    elif selected_method == "Cash":
        st.write("Please have the exact cash ready when you arrive.")
