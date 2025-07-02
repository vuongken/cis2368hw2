import mysql.connector
from mysql.connector import Error
from creds import myCreds

def DBconnection():
    try:
        conn = mysql.connector.connect(
            host=myCreds.host,
            user=myCreds.user,
            password=myCreds.password,
            database=myCreds.database
        )
        print("Database connection successful")
        return conn
    except Error as e:
        print("The error is:", e)
        return None

def execute_read_query(conn, query):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("The error is:", e)
        return []

def execute_query(conn, query, values=None):
    try:
        cursor = conn.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print("The error is:", e)
