import pymysql
from pymysql.cursors import DictCursor
from config import DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        port=DB_PORT,
        cursorclass=DictCursor,
        autocommit=False,
        charset="utf8mb4"
    )


# =========================
# INSERT USER
# =========================
def insert_user(name, email, role="Viewer"):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            # 1. Check duplicate email
            cur.execute("SELECT id FROM users WHERE email=%s", (email,))
            if cur.fetchone():
                conn.rollback()
                return "duplicate"

            # 2. Insert only if not exists
            cur.execute(
                "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)",
                (name, email, role)
            )
            conn.commit()
            return True

    except Exception as e:
        conn.rollback()
        print("Insert error:", e)
        return False

    finally:
        conn.close()


# =========================
# FETCH ALL USERS
# =========================
def get_all_users():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, email, role FROM users")
            return cur.fetchall()
    finally:
        conn.close()


# =========================
# GET USER BY ID
# =========================
def get_user_by_id(user_id):
    conn = get_connection()
    try:
        with conn.cursor(pymysql.cursors.Cursor) as cur:
            cur.execute(
                "SELECT id, name, email, role FROM users WHERE id=%s",
                (user_id,)
            )
            return cur.fetchone()
    finally:
        conn.close()


# =========================
# UPDATE USER
# =========================
def update_user(user_id, name, email, role):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE users SET name=%s, email=%s, role=%s WHERE id=%s",
                (name, email, role, user_id)
            )
        conn.commit()
        return cur.rowcount > 0

    except Exception as e:
        conn.rollback()
        print("Update error:", e)
        return False

    finally:
        conn.close()


# =========================
# DELETE USER
# =========================
def delete_user(user_id):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
        return cur.rowcount > 0

    except Exception as e:
        conn.rollback()
        print("Delete error:", e)
        return False

    finally:
        conn.close()
