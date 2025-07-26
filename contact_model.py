from db_config import get_db_connection

def insert_contact_message(name, email, phone, place, message):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO contact_messages (name, email, phone, place, message) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, email, phone, place, message))
    conn.commit()
    cursor.close()
    conn.close()
def save_contact_form(name, email, phone, subject, message, conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contact_messages (name, email, phone, subject, message) VALUES (%s, %s, %s, %s, %s)",
            (name, email, phone, subject, message)
        )
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error saving contact form:", e)
        return False
