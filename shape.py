from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, size=None, id=None):
        self.size = size
        self.id = id

    @abstractmethod
    def setSize(self):
        pass

    @abstractmethod
    def showInfor(self):
        pass

    @abstractmethod
    def identifyShapeByName(self):
        pass
