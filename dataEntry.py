import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the page
st.set_page_config(page_title="Inventory/Order Management", layout="wide")
st.title("📦 Supply Chain Management Dashboard")

# Styling
st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        background-color: #0073e6;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 40px;
    }
    .stButton>button:hover {
        background-color: #005bb5;
    }
    .card {
        background-color: #f4f4f9;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    h1, h3 {
        color: #333;
    }
    .header {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 18px;
        color: #005bb5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a Navigation Sidebar
with st.sidebar:
    st.header("Navigation")
    section = st.radio("Go to Section", options=["Create Item", "Transfer Ownership", "Update Item State", "View Item Details", "Inventory Overview"])

# Add some dummy data for inventory overview
inventory_data = {
    "Item Name": ["Item A", "Item B", "Item C", "Item D", "Item E"],
    "Stock Level": [100, 150, 75, 120, 60],
    "State": ["Shipped", "Received", "Manufactured", "Delivered", "Created"],
}
df_inventory = pd.DataFrame(inventory_data)

# Overview: Inventory Stock Chart
if section == "Inventory Overview":
    st.markdown("### 📊 Inventory Stock Overview")
    st.write("Stock levels of various items in the supply chain.")
    fig = px.bar(df_inventory, x="Item Name", y="Stock Level", color="State", title="Inventory Stock Overview")
    st.plotly_chart(fig)

# Create Item Section
if section == "Create Item":
    st.markdown("### Create New Item 🏷️")
    with st.form("create_item_form"):
        item_name = st.text_input("Item Name", placeholder="Enter item name")
        item_details = st.text_area("Item Details", placeholder="Enter item details")
        create_item_submit = st.form_submit_button("Create Item")

        if create_item_submit:
            if item_name and item_details:
                st.success(f"Item Created: {item_name}, Details: {item_details}")
            else:
                st.error("Please fill in both the item name and details.")

# Transfer Ownership Section
if section == "Transfer Ownership":
    st.markdown("### Transfer Ownership 🛠️")
    with st.form("transfer_ownership_form"):
        item_id_transfer = st.number_input("Item ID", step=1)
        new_owner_address = st.text_input("New Owner Address", placeholder="Enter new owner address")
        transfer_ownership_submit = st.form_submit_button("Transfer Ownership")

        if transfer_ownership_submit:
            if item_id_transfer and new_owner_address:
                st.success(f"Ownership Transferred: Item ID {item_id_transfer}, New Owner {new_owner_address}")
            else:
                st.error("Please fill in both item ID and new owner address.")

# Update Item State Section
if section == "Update Item State":
    st.markdown("### Update Item State 🔄")
    with st.form("update_state_form"):
        item_id_state = st.number_input("Item ID", step=1)
        item_state = st.selectbox("State", ["Created", "Manufactured", "Shipped", "Received", "Delivered"])
        item_location = st.text_input("Location", placeholder="Enter location")
        update_state_submit = st.form_submit_button("Update State")

        if update_state_submit:
            if item_id_state and item_state and item_location:
                st.success(f"State Updated: Item ID {item_id_state}, State {item_state}, Location {item_location}")
            else:
                st.error("Please fill in all fields.")

# View Item Details Section
if section == "View Item Details":
    st.markdown("### View Item Details 🔍")
    with st.form("view_item_form"):
        view_item_id = st.number_input("Item ID", step=1)
        view_item_submit = st.form_submit_button("View Details")

        if view_item_submit:
            if view_item_id:
                # Mock data for demonstration
                mock_data = {
                    "id": view_item_id,
                    "name": "Sample Item",
                    "state": "Shipped",
                    "location": "Distribution Center",
                    "owner": "0x123456789abcdef",
                }
                st.markdown(
                    f"""
                    **ID:** {mock_data['id']}  
                    **Name:** {mock_data['name']}  
                    **State:** {mock_data['state']}  
                    **Location:** {mock_data['location']}  
                    **Owner:** {mock_data['owner']}
                    """
                )
            else:
                st.error("Please enter a valid item ID.")
