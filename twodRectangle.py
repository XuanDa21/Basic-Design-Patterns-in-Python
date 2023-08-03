from shape import Shape


class twodRectangle(Shape):

    def __init__(self, size=None, id=None):
        super().__init__(size, id)

    def setSize(self, size, id):
        self.size = size
        self.id = id

    def showInfor(self):
        print('2D rectangle has dimension: ' + str(self.size[0]) + ', ' + str(self.size[1]))
        print('Id is ' + str(self.id))
        print("\n    ========================\n")

    def identifyShapeByName(self):
        nameOfShape = "2d rectangle"
        return nameOfShape
