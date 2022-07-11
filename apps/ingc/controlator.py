from ..utils.database import *


BASE_ERROR_MESSAGE = "¡Uy! Actualmente {error_reason}"
BASE_TUTOR_FOUND = "El alumno con código {student_code} tiene como tutor a {tutor_name}. \n Puedes contactarte con dicho tutor en su correo: {tutor_email}"


def validate_student(studentCode):
    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT code FROM students WHERE code='"+studentCode+"'")
    connection.commit()
    data = cursor.fetchall()
    cursor.close()
    result = " ".join(str(x) for x in data)
    result = result.replace("(","").replace(")","").replace(","," ").replace(" ","")
    return result


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


def find_tutor(code):
    connection = mysql.connect()
    cursor = connection.cursor()
    row = cursor.execute("SELECT tutors.name from tutors join students on tutors.id_tutor = students.id_tutor where students.code = '"+code+"'")
    connection.commit()
    tutor_name = cursor.fetchall()
    row2 = cursor.execute("SELECT tutors.email from tutors join students on tutors.id_tutor = students.id_tutor where students.code = '"+code+"'")
    connection.commit()
    tutor_email = cursor.fetchall()
    cursor.close()
    if row == 1 and row2 == 1:
        tutor_name = delete_special_characters(tutor_name)
        tutor_email = delete_special_characters(tutor_email)
        context = BASE_TUTOR_FOUND.format(student_code = code, tutor_name = tutor_name, tutor_email = tutor_email)
        return context
    error_find_tutor_reason = "no cuenta con un tutor, de lo contrario, no se ha actualizado mi base de datos con tu información. Puedes contactarte con nosotros para darte una solución en la sección ¡Contáctate con Nosotros!"
    context = BASE_ERROR_MESSAGE.format(error_reason=error_find_tutor_reason)
    return context


def delete_special_characters(answer):
    result = " ".join(str(x) for x in answer)
    result = result.replace("(","").replace(")","").replace("'","").replace("\\n"," ").replace("\\r"," ").replace("\\"," ")
    result = result.replace(","," ")
    return result
