import db_connection as connection
import mysql.connector as db
from datetime import datetime

class Student:
    
    connection = connection.connection
    myCursor = connection.cursor()
    
    def __init__(self, studentnumber, name, surname, birthdate, gender):
        self.studentnumber = studentnumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        
    def saveStudent(self):
        sql = ("INSERT INTO student (studentnumber,name,surname,birthdate,gender) VALUES (%s,%s,%s,%s,%s)")
        value = (self.studentnumber, self.name, self.surname, self.birthdate, self.gender)
        Student.myCursor.execute(sql, value)
        
        try:
            Student.connection.commit()
            print(f"{Student.myCursor.rowcount} tane kayıt eklendi.")
        except db.Error as err:
            print(f"hata: {err}")
        finally:
            Student.connection.close()
       
    @staticmethod     
    def saveStudents(stdList):
        sql = ("INSERT INTO student (studentnumber,name,surname,birthdate,gender) VALUES (%s,%s,%s,%s,%s)")
        value = stdList
        Student.myCursor.executemany(sql, value)
        
        try:
            Student.connection.commit()
            print(f"{Student.myCursor.rowcount} tane kayıt eklendi.")
        except db.Error as err:
            print(f"hata: {err}")
        finally:
            Student.connection.close()

'''
furkan = Student(20202020006, "furkan", "zekiri", datetime(2002, 3, 9), "E")
furkan.saveStudent()
'''

'''
stdList = [
    (20202020013, "sefa", "geyik", datetime(2002, 2, 9), "E"),
    (20202020031, "emir", "tonkal", datetime(2002, 2, 12), "E"),
    (20202020069, "ömer kadir", "kurt", datetime(2002, 1, 4), "E"),
]
Student.saveStudents(stdList)
'''