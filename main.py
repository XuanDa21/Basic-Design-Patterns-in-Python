import array

from system import system

sys = system()


def getSizeRec(is3D):
    size = array.array('d', [])
    if is3D:
        h = float(input('Value of height: '))
        w = float(input('Value of width: '))
        a = float(input('Value of length: '))
        size.append(h)
        size.append(w)
        size.append(a)
    else:
        h = float(input('Value of height: '))
        w = float(input('Value of width: '))
        size.append(h)
        size.append(w)
    return size


def getSizeCir():
    size = array.array('d', [])
    r = float(input('Value of radius: '))
    size.append(r)
    return size


def setSizeShape(size):
    sys.setSize(size)


def getShape(is3D):
    print("""
        r - Rectangle
        c - circle
    """)
    c = input('Enter here: ')
    if c == "r":
        sys.setRectangleShape()
        setSizeShape(getSizeRec(is3D))
    elif c == "c":
        sys.setCircleShape()
        setSizeShape(getSizeCir())
    else:
        print("Invalid input!")


def addShape():
    print("""
        1. 2D
        2. 3D
    """)
    ans = input("What would you like to do? ")
    is3D = False
    if ans == "1":
        sys.setFactory("2D")
        getShape(is3D)
    else:
        is3D = True
        sys.setFactory("3D")
        getShape(is3D)


def getIdShape(choice):
    id = 0
    if choice == "2":
        id = int(input("Enter Id shape to delete: "))
    elif choice == "4":
        id = int(input("Enter Id shape to modify: "))
    return id


def getSizeShapeToModify(shapeType):
    size = []
    is3D = False
    if shapeType == 1 or shapeType == 2:
        size = getSizeCir()
    elif shapeType == 4:
        is3D = True
        size = getSizeRec(is3D)
    else:
        size = getSizeRec(is3D)
    return size


def main():
    while True:
        print("""
        1. Add a new shape
        2. Delete a shape
        3. Show shape list
        4. Modify shape
        5. Undo
        6. Redo
        7. Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            addShape()
            print("\n Shape Added!")

        elif ans == "2":
            id = getIdShape(ans)
            if sys.deleteShape(id):
                print("Invalid ID!")
            else:
                print("\n Shape Deleted!")

        elif ans == "3":
            print("\n    ========================\n")
            sys.showInfor()

        elif ans == "4":
            id = getIdShape(ans)
            shapeType = sys.findShapeType(id)
            if shapeType == 0:
                print("Invalid id!")
            else:
                size = getSizeShapeToModify(shapeType)
                sys.modifyShape(size)
                print("\n Shape modified!")

        elif ans == "5":
            if sys.undo() == True:
                print("Nothing To UNDO")

        elif ans == "6":
            if sys.redo() == True:
                print("Nothing To REDO")

        elif ans == "7":
            print("\n Goodbye!")
            exit(0)

        elif ans != "":
            print("\n Not Valid Choice Try again")


if __name__ == "__main__":
    main()
