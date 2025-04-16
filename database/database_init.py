import mysql.connector
from mysql.connector import Error
import os

def create_database():
    try:
        # Connect without specifying database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )
        
        cursor = connection.cursor()
        
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS student_information_system")
        
        print("Database created successfully")
        return connection
        
    except Error as e:
        print(f"Error creating database: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def create_tables():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="student_information_system"
        )
        
        cursor = connection.cursor()
        

        # Colleges table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS colleges (
            college_code VARCHAR(20) PRIMARY KEY,
            college_name VARCHAR(100) NOT NULL
        )
        """)

        # Programs table 
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS programs (
            program_code VARCHAR(20) PRIMARY KEY,
            program_name VARCHAR(100) NOT NULL,
            college_code VARCHAR(20) NULL,
            FOREIGN KEY (college_code) REFERENCES colleges(college_code)
        )
        """)

        # Students table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id VARCHAR(9) PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            year_level VARCHAR(20) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            program_code VARCHAR(20) NULL,
            FOREIGN KEY (program_code) REFERENCES programs(program_code)
        )
        """)
        
 
        
        
        connection.commit()
        print("Tables created successfully")
        
    except Error as e:
        print(f"Error creating tables: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
    create_tables()