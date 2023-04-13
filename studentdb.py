import sqlite3
from sqlite3 import Error



class Students:
    def __init__(self, path):
        self.connection = None
        try:
            self.connection = sqlite3.connect(path)
            cursor = self.connection.cursor()
            cursor.execute("""
               CREATE TABLE IF NOT EXISTS students (
                 student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 department TEXT NOT NULL,
                 mark1 INTEGER NOT NULL,
                 mark2 INTEGER NOT NULL,
                 mark3 INTEGER NOT NULL
               );
               """)
            self.connection.commit()
            print("Connection to SQLite DB successfull")
        except Error as e:
            print(f"The error '{e}' occured")

    def addStudent(self, name, department, mark1, mark2, mark3):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(f"""
            INSERT INTO students (name, department, mark1, mark2, mark3) VALUES 
            ('{name}', '{department}', '{mark1}', '{mark2}', '{mark3}') 
            """)
            self.connection.commit()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def otchisl(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
            DELETE FROM students WHERE (mark1 + mark2 + mark3) / 3.0 < 3.5
            """)
            self.connection.commit()
        except Error as e:
            print(f"The error '{e}' occurred")

    def getStudents(self):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute("""SELECT * FROM students""")
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    def close(self):
        self.connection.close()
