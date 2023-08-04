import random

from factoryMaker import factoryMaker
from shapeType import shapeType

shapesBefore = []
shapesAfter = []
temp = []


class system:

    # private variables
    __factory = None
    __shape = None
    __shapes = None
    __sizeBeforeModi = None
    __tempId = None
    __factoryMaker = None


    def __init__(self, factory=None, shape=None):
        self.__factory = factory
        self.__shape = shape
        self.__shapes = shapesBefore
        self.__sizeBeforeModi = None
        self.__tempId = None
        self.__factoryMaker = factoryMaker

    def __getitem__(self, index):
        return self.__shapes[index]

    def setFactory(self, type):
        self.__factory = self.__factoryMaker.get_instance().getFactory(type)

    def setRectangleShape(self):
        self.__shape = self.__factory.get_instance().getShape("Rectangle")

    def setCircleShape(self):
        self.__shape = self.__factory.get_instance().getShape("Circle")

    def setSize(self, size):
        id = random.randint(1, 50)
        self.__shape.setSize(size, id)
        shapesBefore.append((id, self.__shape, size))
        shapesAfter.append((shapesBefore[-1], "add"))

    def showInfor(self):
        for index in range(0, len(self.__shapes)):
            self.__getitem__(index)[1].showInfor()

    def deleteShape(self, id):
        isError = True
        index = -1
        for pair in shapesBefore:
            index += 1
            if pair[0] == id:
                shapesAfter.append((pair, "delete", index))
                isError = False
                shapesBefore.remove(pair)
        return isError

    def findShapeType(self, id):
        type = 0
        self.__tempId = id
        for pair in shapesBefore:
            if pair[0] == id:
                if pair[1].identifyShapeByName() == "2d circle":
                    type = shapeType['circle2d'].value
                elif pair[1].identifyShapeByName() == "2d rectangle":
                    type = shapeType['rectangle2d'].value
                elif pair[1].identifyShapeByName() == "3d rectangle":
                    type = shapeType['rectangle3d'].value
                elif pair[1].identifyShapeByName() == "3d circle":
                    type = shapeType['circle3d'].value
                self.__sizeBeforeModi = pair[2]
        return type

    def modifyShape(self, sizeAfterModi):
        for pair in shapesBefore:
            if pair[0] == self.__tempId:
                pair[1].setSize(sizeAfterModi, self.__tempId)
        shapesAfter.append((self.__sizeBeforeModi, self.__tempId, "modify", sizeAfterModi))

    def undo(self):
        isError = False
        if len(shapesAfter):
            if shapesAfter[-1][1] == "delete":
                # if shapesAfter[0][1] == "add":
                #     shapesAfter.pop(0)
                shapesBefore.insert(shapesAfter[-1][2], shapesAfter[-1][0])
                temp.append(shapesAfter[-1])
                shapesAfter.pop()
            elif shapesAfter[-1][1] == "add":
                shapesBefore.remove(shapesAfter[-1][0])
                temp.append(shapesAfter[-1])
                shapesAfter.pop()
            elif shapesAfter[-1][2] == "modify":
                if shapesAfter[0][1] == "add":
                    shapesAfter.pop(0)
                for pair in shapesBefore:
                    if pair[0] == shapesAfter[-1][1]:
                        pair[1].setSize(shapesAfter[-1][0], pair[0])
                        temp.append(shapesAfter[-1])
                        shapesAfter.pop()
                        break
        else:
            isError = True
        return isError

    def redo(self):
        isError = False
        if len(temp):
            if temp[-1][1] == "delete":
                shapesBefore.remove(temp[-1][0])
                shapesAfter.append(temp[-1])
                temp.pop()
            elif temp[-1][1] == "add":
                shapesBefore.append(temp[-1][0])
                shapesAfter.append(temp[-1])
                temp.pop()
            elif temp[-1][2] == "modify":
                for pair in shapesBefore:
                    if pair[0] == temp[-1][1]:
                        pair[1].setSize(temp[-1][3], pair[0])
                        shapesAfter.append(temp[-1])
                        temp.pop()
                        break
        else:
            isError = True
        return isError
