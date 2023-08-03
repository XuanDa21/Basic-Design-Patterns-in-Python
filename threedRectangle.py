from shape import Shape


class threedRectangle(Shape):

    def __init__(self, size=None, id=None):
        super().__init__(size, id)

    def setSize(self, size, id):
        self.size = size
        self.id = id

    def showInfor(self):
        print('3D Rectangle has dimension: ' + str(self.size[0]) + ', ' + str(self.size[1]) + ', ' + str(self.size[2]))
        print('Id is ' + str(self.id))
        print("\n    ========================\n")

    def identifyShapeByName(self):
        nameOfShape = "3d rectangle"
        return nameOfShape
