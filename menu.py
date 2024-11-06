import streamlit as st

def menu_page():
    menu_items = [
        {"name": "Adobo", "price": 11410.00, "image": "https://i.ibb.co/Pt0GVMM/adobo.jpg"},
        {"name": "Sinigang", "price": 1200000.00, "image": "https://i.ibb.co/SyF3H94/bicol.jpg"},
        {"name": "Bicol Express", "price": 150000.00, "image": "https://i.ibb.co/4gkwL7d/sinigang.jpg"},
    ]
    
    st.title("Menu")

    # Display menu items with checkboxes
    selected_items = []  # Store selected items

    for item in menu_items:
        col1, col2, col3 = st.columns([1, 1, 3])
        
        with col1:
            st.image(item["image"], width=100)
        with col2:
            st.write(f"**{item['name']}**")
        with col3:
            st.write(f"Price: ${item['price']:,.2f}")
        
        # Add checkbox for each item
        is_selected = st.checkbox(f"Select {item['name']} - ${item['price']:,.2f}", key=item["name"])
        
        if is_selected:
            selected_items.append(item)  # Add selected item to list

    # Order and Clear Orders buttons
    if st.button("Order"):
        if selected_items:
            # Pass selected items to session state for Billing tab
            st.session_state['ordered_items'] = selected_items
            st.success("Order placed! Proceeding to Billing...")
            # Navigate to the Billing tab
            st.query_params.tab = "Billing Method"
        else:
            st.warning("Please select at least one item to order.")

    if st.button("Clear Orders"):
        # Clear selected items by resetting session state
        for item in menu_items:
            st.session_state[item["name"]] = False  # Reset checkbox state
        st.experimental_rerun()  # Refresh to update checkbox states
