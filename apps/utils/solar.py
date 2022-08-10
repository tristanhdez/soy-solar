from ..utils.database import *


BASE_ERROR_MESSAGE = "¡Uy! Actualmente {error_reason}"


class Solar:


    def __init__(self, keywords):
        self.keywords = keywords


    def find_answer(self, keywords):
        return f"{keywords}"


class Question(Solar):


    def find_answer(self):
        connection = mysql.connect()
        cursor = connection.cursor()
        row = cursor.execute("SELECT answer, link FROM questions WHERE keyword='"+str(self.keywords)+"'")
        connection.commit()
        answer = cursor.fetchall()
        cursor.close()
        if row == 1:
            return super().find_answer(keywords=answer)
        error_find_answer_reason = "no tenemos esa información en nuestra base de datos, nos apoyarías muchísimo si colaboras con tu pregunta en la sección: ¡Colabora una Pregunta!"
        context = BASE_ERROR_MESSAGE.format(error_reason=error_find_answer_reason)
        return super().find_answer(keywords=context)
