from threedFactory import threedFactory
from twodFactory import twodFactory


class factoryMaker:

    def __init__(self, twodFactory=twodFactory(), threedFactory=threedFactory()):
        self.twodFactory = twodFactory
        self.threedFactory = threedFactory

    _instance = None
    @staticmethod
    def get_instance():
        if factoryMaker._instance is None:
            factoryMaker._instance = factoryMaker()
        return factoryMaker._instance

    def getFactory(self, type):
        if type == "2D":
            factoryType = self.twodFactory.get_instance()
        else:
            factoryType = self.threedFactory.get_instance()
        return factoryType
