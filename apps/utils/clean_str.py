class Clean_Str():


    def __init__(self, str):
        self.str = str


    def cleaned(self, str):
        return str(str)


class Clean(Clean_Str):


    def cleaned(self):
        result = self.str.replace("(","").replace(")","").replace("'","")\
        .replace('\\n', '\n').replace('\\t', '\t').replace("\\r","\r").replace("\\"," ").replace(","," ")
        return result
