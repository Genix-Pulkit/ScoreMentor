from reg_login import SignIn
from tkinter import *
import mysql.connector as connector
import sys

def connect_to_database():
    try:
        connection = connector.connect(
            host="localhost",
            user="root",
            password="dpsb"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS scorementor")
            connection.database = "scorementor"    
        return connection

    except connector.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit()
        return None
    
def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Courses (id INT AUTO_INCREMENT, name VARCHAR(255), duration VARCHAR(100), fees INT, description VARCHAR(255), PRIMARY KEY(id))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Students (roll_no INT AUTO_INCREMENT, name VARCHAR(255), email VARCHAR(255), gender VARCHAR(255), state VARCHAR(255), address VARCHAR(255), dob VARCHAR(255), contact VARCHAR(255), adm_date VARCHAR(255), course VARCHAR(255), city VARCHAR(255), pin INT, PRIMARY KEY(roll_no))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Results (id INT AUTO_INCREMENT, roll_no INT, name VARCHAR(255), course VARCHAR(255), max_marks INT, marks_obt INT, PRIMARY KEY(id), FOREIGN KEY(roll_no) REFERENCES Students(roll_no))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (id INT AUTO_INCREMENT, username VARCHAR(255), password VARCHAR(255),email VARCHAR(255), age INT, PRIMARY KEY (id))")    
    connection.commit()

if __name__ == "__main__":
    connection = connect_to_database()
    create_tables(connection)
    root = Tk()
    SignIn(root, connection)
    root.mainloop()
