inputFile = open("Day3\inputFile.txt","r")

inputTestFile = open("Day3\inputTestFile.txt","r")
Lines = inputFile.readlines()

def problem1():
    """
    You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
    The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:
    From your starting position at the top-left, check the position that is right 3 and down 1. 
    Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
    """
    countTrees = 0
    XCoordinate = 0

    for line in Lines:
        XCoordinate = XCoordinate % 31
        currentInput = line.strip()
        currentValueAtXCoordinate = currentInput[XCoordinate]
        if (currentValueAtXCoordinate == "#"):
            countTrees = countTrees +1
    
        XCoordinate = XCoordinate +3
    
    print(countTrees)


def problem2Helper(XCoordinateStep, YCoordinateStep):
    """

    """
    countTrees = 0
    YCoordinate = 0
    XCoordinate = 0

    for line in Lines:
        if (YCoordinate%YCoordinateStep == 0):
            XCoordinate = XCoordinate % 31
            currentInput = line.strip()
            currentValueAtXCoordinate = currentInput[XCoordinate]
            if (currentValueAtXCoordinate == "#"):
                countTrees = countTrees +1
            XCoordinate = XCoordinate + XCoordinateStep

        YCoordinate = YCoordinate +1    
    return countTrees


def problem2():
    """
        Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (Problem 1)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    What do you get if you multiply together the number of trees encountered on each of the listed slopes?
    """
    result = problem2Helper(1,1) * problem2Helper(3,1) * problem2Helper(5,1) * problem2Helper(7,1) *problem2Helper(1,2)
    print(result)


problem2()