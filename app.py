import streamlit as st
import pandas as pd
from db import (
    get_all_users,
    insert_user,
    update_user,
    delete_user,
    get_user_by_id
)

st.set_page_config(page_title="User Management System", layout="centered")


menu = ["Add User", "View Users", "Update User", "Delete User"]
choice = st.sidebar.selectbox("Menu", menu)

# Add User

if choice == "Add User":
    st.subheader("Add New User")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    role = st.selectbox("Role", ["Admin", "Manager", "Viewer"])

    if st.button("Add User"):
        if name and email:
            insert_user(name, email, role)
            st.success(f"User '{name}' added successfully!")
        else:
            st.error("Please fill all fields.")

# View Users

elif choice == "View Users":
    st.subheader("All Users")

    users = get_all_users()
    df = pd.DataFrame(users, columns=["ID", "Name", "Email", "Role"])

    st.dataframe(df, use_container_width=True)

# Update User

elif choice == "Update User":
    st.subheader("Update User")

    users = get_all_users()
    user_ids = [u["id"] for u in users]


    selected_id = st.selectbox("Select User ID to Update", user_ids)

    user = get_user_by_id(selected_id)

    if user:
        new_name = st.text_input("Full Name", user[1])
        new_email = st.text_input("Email", user[2])
        new_role = st.selectbox("Role", ["Admin", "Manager", "Viewer"], index=["Admin", "Manager", "Viewer"].index(user[3]))

        if st.button("Update User"):
            update_user(selected_id, new_name, new_email, new_role)
            st.success(f"User ID {selected_id} updated successfully!")

# Delete User

elif choice == "Delete User":
    st.subheader("Delete User")

    users = get_all_users()
    user_ids = [u[0] for u in users]

    selected_id = st.selectbox("Select User ID to Delete", user_ids)

    if st.button("Delete"):
        delete_user(selected_id)
        st.success(f"User ID {selected_id} deleted successfully!")

