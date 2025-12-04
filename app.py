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
            st.rerun() 
        else:
            st.error("Please fill all fields.")

# View Users
elif choice == "View Users":
    st.subheader("All Users")

    users = get_all_users()
    if users:
        df = pd.DataFrame(users)
        df = df[["id", "name", "email", "role"]]  
        df.columns = ["ID", "Name", "Email", "Role"]  
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No users found.")

# Update User
elif choice == "Update User":
    st.subheader("Update User")

    users = get_all_users()
    
    if users:
        # Create user display list
        user_options = {f"{u['id']} - {u['name']}": u['id'] for u in users}
        
        selected_display = st.selectbox("Select User to Update", list(user_options.keys()))
        selected_id = user_options[selected_display]

        user = get_user_by_id(selected_id)

        if user:
            new_name = st.text_input("Full Name", user[1])
            new_email = st.text_input("Email", user[2])
            new_role = st.selectbox("Role", ["Admin", "Manager", "Viewer"], 
            index=["Admin", "Manager", "Viewer"].index(user[3]))

            if st.button("Update User"):
                update_user(selected_id, new_name, new_email, new_role)
                st.success(f"User '{new_name}' updated successfully!")
                st.rerun()  
    else:
        st.info("No users available to update.")

# Delete User
elif choice == "Delete User":
    st.subheader("Delete User")

    users = get_all_users()
    
    if users:
        # Create user display list
        user_options = {f"{u['id']} - {u['name']}": u['id'] for u in users}
        
        selected_display = st.selectbox("Select User to Delete", list(user_options.keys()))
        selected_id = user_options[selected_display]

        if st.button("Delete", type="primary"):
            delete_user(selected_id)
            st.success(f"User deleted successfully!")
            st.rerun()  
    else:
        st.info("No users available to delete.")