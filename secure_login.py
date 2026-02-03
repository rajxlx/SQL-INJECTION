import mysql.connector

def secure_login(username, password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prince@sql3110
        database="siege_db"
    )

    cursor = db.cursor(prepared=True)
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()
    db.close()
    return result
