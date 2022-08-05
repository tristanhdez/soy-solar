from ..utils.database import *


BASE_ERROR_MESSAGE = "¡Uy! Actualmente {error_reason}"
BASE_TUTOR_FOUND = "El alumno con código {student_code} tiene como tutor a {tutor_name}. \n Puedes contactarte con dicho tutor en su correo: {tutor_email}"


class Tutor:


    def __init__(self, code):
        self.code = code

    def find_tutor(self, code):
        return f"{code}"



class Get_Tutor(Tutor):

    def find_tutor(self):
        connection = mysql.connect()
        cursor = connection.cursor()
        row = cursor.execute("SELECT tutors.name from tutors join students on tutors.id_tutor = students.id_tutor where students.code = '"+self.code+"'")
        connection.commit()
        tutor_name = cursor.fetchall()
        row2 = cursor.execute("SELECT tutors.email from tutors join students on tutors.id_tutor = students.id_tutor where students.code = '"+self.code+"'")
        connection.commit()
        tutor_email = cursor.fetchall()
        cursor.close()
        if row == 1 and row2 == 1:
            context = BASE_TUTOR_FOUND.format(student_code = self.code, tutor_name = tutor_name, tutor_email = tutor_email)
            return super().find_tutor(code=context)
        error_find_tutor_reason = "no cuenta con un tutor, de lo contrario, no se ha actualizado mi base de datos con tu información. Puedes contactarte con nosotros para darte una solución en la sección ¡Contáctate con Nosotros!"
        context = BASE_ERROR_MESSAGE.format(error_reason=error_find_tutor_reason)
        return super().find_tutor(code=context)
