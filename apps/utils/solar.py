from ..utils.database import *


BASE_ERROR_MESSAGE = "¡Uy! Actualmente {error_reason}"


class Solar:


    def __init__(self, question):
        self.question = question


    def find_answer(self, question):
        return f"{question}"


class Question(Solar):


    def find_answer(self):
        connection = mysql.connect()
        cursor = connection.cursor()
        row = cursor.execute("SELECT answer FROM questions WHERE keyword='"+str(self.question)+"'")
        connection.commit()
        answer = cursor.fetchall()
        cursor.close()
        if row == 1:
            return super().find_answer(question=answer)
        error_find_answer_reason = "no tenemos esa información en nuestra base de datos, nos apoyarías muchísimo si colaboras con tu pregunta en la sección: ¡Colabora una Pregunta!"
        context = BASE_ERROR_MESSAGE.format(error_reason=error_find_answer_reason)
        return super().find_answer(question=context)


