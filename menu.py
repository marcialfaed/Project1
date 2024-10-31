import streamlit as st

def menu_page():
    menu_items = [
        {"name": "Adobo", "price": "$11,410.00", "image": "https://i.ibb.co/Pt0GVMM/adobo.jpg"},
        {"name": "Sinigang", "price": "$1,200,000.00", "image": "https://i.ibb.co/SyF3H94/bicol.jpg"},
        {"name": "Bicol Express", "price": "$150,000.00", "image": "https://i.ibb.co/4gkwL7d/sinigang.jpg"},
    ]
    st.title("Menu")
    for item in menu_items:
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            st.image(item["image"], width=100)
        with col2:
            st.write(f"**{item['name']}**")
        with col3:
            st.write(f"Price: {item['price']}")
