import streamlit as st
import pandas as pd
from db import (
    get_all_users,
    insert_user,
    update_user,
    delete_user,
    get_user_by_id
)

st.set_page_config(
    page_title="User Management System",
    layout="centered"
)

menu = ["Add User", "View Users", "Update User", "Delete User"]
choice = st.sidebar.selectbox("Menu", menu)

# --------------------------------------------------
# ADD USER
# --------------------------------------------------
if choice == "Add User":
    st.subheader("➕ Add New User")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    role = st.selectbox("Role", ["Admin", "Manager", "Viewer"])

    if st.button("Add User"):
        if not name or not email:
            st.error("Please fill all fields.")
        else:
            result = insert_user(name, email, role)

            if result is True:
                @st.dialog("✅ Success")
                def add_success_dialog():
                    st.success(f"New user **{name}** has been added successfully.")
                    if st.button("OK"):
                        st.rerun()

                add_success_dialog()

            elif result == "duplicate":
                st.warning("A user with this email already exists.")

            else:
                st.error("Failed to add user.")


# --------------------------------------------------
# VIEW USERS
# --------------------------------------------------
elif choice == "View Users":
    st.subheader("📋 All Users")

    users = get_all_users()

    if users:
        df = pd.DataFrame(users)
        df = df[["id", "name", "email", "role"]]
        df.columns = ["ID", "Name", "Email", "Role"]
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No users found.")


# --------------------------------------------------
# UPDATE USER
# --------------------------------------------------
elif choice == "Update User":
    st.subheader("✏️ Update User")

    users = get_all_users()

    if not users:
        st.info("No users available to update.")
    else:
        user_options = {
            f"{u['id']} - {u['name']}": u['id'] for u in users
        }

        selected_display = st.selectbox(
            "Select User to Update",
            list(user_options.keys())
        )

        selected_id = user_options[selected_display]
        user = get_user_by_id(selected_id)

        if user:
            new_name = st.text_input("Full Name", user[1])
            new_email = st.text_input("Email", user[2])
            new_role = st.selectbox(
                "Role",
                ["Admin", "Manager", "Viewer"],
                index=["Admin", "Manager", "Viewer"].index(user[3])
            )

            if st.button("Update User"):
                result = update_user(
                    selected_id,
                    new_name,
                    new_email,
                    new_role
                )

                if result:
                    @st.dialog("✏️ Update Successful")
                    def update_success_dialog():
                        st.success(
                            f"User **{new_name}** has been updated successfully."
                        )
                        if st.button("OK"):
                            st.rerun()

                    update_success_dialog()
                else:
                    st.error("Failed to update user.")


# --------------------------------------------------
# DELETE USER
# --------------------------------------------------
elif choice == "Delete User":
    st.subheader("🗑️ Delete User")

    users = get_all_users()

    if not users:
        st.info("No users available to delete.")
    else:
        user_options = {
            f"{u['id']} - {u['name']}": u['id'] for u in users
        }

        selected_display = st.selectbox(
            "Select User to Delete",
            list(user_options.keys())
        )

        selected_id = user_options[selected_display]

        if st.button("Delete", type="primary"):
            result = delete_user(selected_id)

            if result:
                @st.dialog("🗑️ User Deleted")
                def delete_success_dialog():
                    st.success("The user has been deleted successfully.")
                    if st.button("OK"):
                        st.rerun()

                delete_success_dialog()
            else:
                st.error("Failed to delete user.")
