from ..utils.database import *

# Base Error Message when we don't found any answer
BASE_ERROR_MESSAGE = "¡Uy! Actualmente {error_reason}"


class Solar:


    """

    A class used to get the questions and find the answers
    ...


    Attributes
    ----------
    keywords : str
        a formatted string to get the question of the user


    Methods
    -------
    find_answer(keywords=keywords)
        Prints the answers of the question asked by user

    """


    def __init__(self, keywords):
        """
        Parameters
        ----------
        keywords : str
            The question of the user
        """
        self.keywords = keywords


    def find_answer(self, keywords):
        """Return a string with the answer

        Args:
            keywords (str): getting the string of answer

        Returns:
            str: Answer
        """
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
