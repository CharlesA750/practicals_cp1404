class ProgrammingLanguage:
    """create a class for programing languages"""
    def __init__(self,name,typing,reflection,year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{},{} typing, reflection is {}, released in {}".format(self.name,self.typing,self.reflection,self.year)

    def is_dynamic(self):
        if self.typing.lower() == "dynamic":
            return True
        else:
            return False