import mysql.connector

def vulnerable_login(username, password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prince@sql3110",
        database="siege_db"
    )

    cursor = db.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    result = cursor.fetchone()
    db.close()
    print("EXECUTED QUERY:", query)
    return result
