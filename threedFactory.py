from threedCircle import threedCircle
from threedRectangle import threedRectangle


class threedFactory:
    # _instance is a privated data members
    __instance = None

    @staticmethod
    def get_instance():
        if threedFactory.__instance is None:
            threedFactory.__instance = threedFactory()
        return threedFactory.__instance

    def getShape(self, type):
        self.type = type
        if self.type == "Circle":
            Shape = threedCircle()
        else:
            Shape = threedRectangle()
        return Shape
