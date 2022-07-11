from ..utils.database import *


BASE_ERROR_MESSAGE = "¡Uy! Actualmente {error_reason}"


def find_answer(question):
    connection = mysql.connect()
    cursor = connection.cursor()
    row = cursor.execute("SELECT answer FROM questions WHERE keyword='"+question+"'")
    connection.commit()
    answer = cursor.fetchall()
    cursor.close()
    if row == 1:
        return answer
    error_find_answer_reason = "no tenemos esa información en nuestra base de datos, nos apoyarías muchísimo si colaboras con tu pregunta en la sección: ¡Colabora una Pregunta!"
    context = BASE_ERROR_MESSAGE.format(error_reason=error_find_answer_reason)
    return context


def delete_special_characters(answer):
    result = " ".join(str(x) for x in answer)
    result = result.replace("(","").replace(")","").replace("'","").replace("\\n"," ").replace("\\r"," ").replace("\\"," ")
    result = result.replace(","," ")
    return result
