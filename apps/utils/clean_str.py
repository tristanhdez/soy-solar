class Clean_Str():


    """

    A class used to clean string from an tuple deleting special characters like:
    (),.""''
    ...


    Attributes
    ----------
    str : str
        a formatted string to get the string to clean


    Methods
    -------
    cleaned(keywords=keywords)
        Return the string cleaned

    """

    def __init__(self, str):
        """
        Parameters
        ----------
        keywords : str
            The message/string to clean
        """
        self.str = str


    def cleaned(self, str):
        """Return string cleaned

        Args:
            str (str): getting the string cleaned

        Returns:
            str: string/message cleaned for special characters
        """
        return str(str)


class Clean(Clean_Str):


    def cleaned(self):
        result = self.str.replace("(","").replace(")","").replace("'","") \
            .replace('\\n', '\n').replace('\\t', '\t').replace("\\r","\r") \
                .replace("\\"," ").replace(","," ")
        return result
