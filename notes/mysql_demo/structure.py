import db_connection as connection
import mysql.connector as db
from datetime import datetime

class Student:
    
    connection = connection.connection
    myCursor = connection.cursor()
    
    def __init__(self, id, studentnumber, name, surname, birthdate, gender):
        if id == None:
            self.id = 0
        else:
            self.id = id
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

    @staticmethod
    def getStudents():
        #sql = "select * from student where gender like '%K%' and surname like '%e%' order by name,surname"
        sql = "select * from student"
        Student.myCursor.execute(sql)
        
        try:
            infoList = Student.myCursor.fetchall()
            for std in infoList:
                print(std)
        except db.Error as err:
            print(f"hata: {err}")
        finally:
            Student.connection.close()
    
    @staticmethod
    def getStudentbyId(id):
        sql = "select * from student where id = %s"
        value = (id,)
        Student.myCursor.execute(sql, value)
        
        try:
            obj = Student.myCursor.fetchone()
            return Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5])
        except db.Error as err:
            print(f"hata: {err}")
            
    def updateStudent(self):
        sql = "update student set studentnumber = %s, name = %s, surname = %s, birthdate = %s, gender = %s where id = %s"
        value = (self.studentnumber, self.name, self.surname, self.birthdate, self.gender, self.id)
        Student.myCursor.execute(sql, value)
        
        try:
            Student.connection.commit()
            print(f"{Student.myCursor.rowcount} tane kayıt güncellendi.")
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
    (20202020069, "ömer kadir", "kurt", datetime(2000, 1, 4), "E"),
    (20202023013, "rümeysa", "tuncer", datetime(2002, 1, 31), "K"),
    (20222020031, "asya", "pekşen", datetime(2002, 11, 27), "K"),
    (20202020569, "talha", "demir", datetime(2002, 4, 5), "E"),
    (20202620013, "sedat cem", "kızıltoprak", datetime(2002, 4, 29), "E"),
    (20132020031, "aylin", "karakaş", datetime(2002, 7, 23), "K"),
]
Student.saveStudents(stdList)
'''

'''
Student.info()
'''

'''
std = Student.getStudentbyId(2)
std.surname = "zex"

std.updateStudent()
'''