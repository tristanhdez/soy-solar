from ..utils.database import *


class Keywords():


    def __init__(self) -> None:
        pass


    def find_keywords(self):
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT keyword_human, description FROM questions;")
        connection.commit()
        data = cursor.fetchall()
        cursor.close()
        return data
