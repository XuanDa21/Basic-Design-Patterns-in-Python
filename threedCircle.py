from shape import Shape


class threedCircle(Shape):

    def __init__(self, size=None, id=None):
        super().__init__(size, id)

    def setSize(self, size, id):
        self.size = size
        self.id = id

    def showInfor(self):
        print('3D Circle has radius is ' + str(self.size[0]) + ', id is ' + str(self.id))
        print("\n    ========================\n")

    def identifyShapeByName(self):
        nameOfShape = "3d circle"
        return nameOfShape
