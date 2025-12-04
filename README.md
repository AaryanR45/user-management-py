# User Management System with Streamlit and MySQL

## Project Overview
This project is a simple **User Management System** built using **Streamlit** for the frontend and **MySQL** for the backend. It allows you to perform full **CRUD operations** on users, including assigning roles.

---

## Features
- Add new users with Name, Email, and Role.
- View all users in a table.
- Update existing user information.
- Delete users.
- Fully functional Streamlit UI.
- MySQL backend with a simple schema.

---

## Project Structure
```
user-management/
│
├── app.py              # Streamlit frontend UI
├── db.py               # Database operations (CRUD functions)
├── config.py           # Database configuration
├── schema.sql          # SQL script to create database and table
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── user.ipynb          # Jupyter notebook to setup database
```

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/username/user-management.git
cd user-management
```

### 2. Create and activate a virtual environment
**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```
**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Set up the database
1. Make sure MySQL server is running.
2. Open `user.ipynb` in Jupyter Notebook.
3. Run the notebook cells to create the database and `users` table.

Alternatively, you can run `schema.sql` manually in a MySQL client.

### 5. Configure database connection
Edit `config.py` with your MySQL credentials:
```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "usermgmt"
DB_PORT = 3306
```

---

## Running the App
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to access the app.

---

## Usage
1. **Add User**: Enter Name, Email, and select Role, then click "Add User".
2. **View Users**: Displays a table of all users.
3. **Update User**: Select a user ID, modify details, and update.
4. **Delete User**: Select a user ID and delete.

---

