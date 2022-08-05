from ..utils.database import *


class Student():

    def __init__(self, code):
        self.code = code


    def validate_student(self, code):
        return f"{code}"


class Validate(Student):


    def validate_student(self):
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT code FROM students WHERE code='"+self.code+"'")
        connection.commit()
        data = cursor.fetchall()
        cursor.close()
        return super().validate_student(code = data)
