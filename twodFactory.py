from twodCircle import twodCircle
from twodRectangle import twodRectangle


class twodFactory:
    # _instance is a privated data members,
    # A static method is also a method that is bound to the class and not the object of the class
    __instance = None

    @staticmethod
    def get_instance():
        if twodFactory.__instance is None:
            twodFactory.__instance = twodFactory()
        return twodFactory.__instance

    def getShape(self, type):
        self.type = type
        if self.type == "Circle":
            Shape = twodCircle()
        else:
            Shape = twodRectangle()
        return Shape
