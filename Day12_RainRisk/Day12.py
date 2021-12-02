def changeDirection(currentDirection, instruction):
    change = int(int(instruction[1:]) / 90)
    if instruction[0] == "R":
        change = -change
    if currentDirection == "N":
        possibleDirections = ["N", "W", "S", "E"]
    elif currentDirection == "S":
        possibleDirections = ["S", "E", "N", "W"]
    elif currentDirection == "E":
        possibleDirections = ["E", "N", "W", "S"]
    elif currentDirection == "W":
        possibleDirections = ["W", "S", "E", "N"]
    return(possibleDirections[change])


def q1(inputLines):
    positionNorthSouth = 0
    positionEastWest = 0
    currentDirection = "E"
    for line in inputLines:
        if line[0] == "N":
            positionNorthSouth += int(line[1:])
        elif line[0] == "S":
            positionNorthSouth -= int(line[1:])
        elif line[0] == "E":
            positionEastWest += int(line[1:])
        elif line[0] == "W":
            positionEastWest -= int(line[1:])
        elif line[0] == "F":
            if currentDirection == "N":
                positionNorthSouth += int(line[1:])
            elif currentDirection == "S":
                positionNorthSouth -= int(line[1:])
            elif currentDirection == "E":
                positionEastWest += int(line[1:])
            elif currentDirection == "W":
                positionEastWest -= int(line[1:])
        elif line[0] == "L" or line[0] == "R":
            currentDirection = changeDirection(currentDirection, line)

    return(abs(positionNorthSouth)+abs(positionEastWest))


if __name__ == "__main__":
    with open("Day12_RainRisk/Input.txt") as input:
        inputLines = [str(line.strip()) for line in input]

    result_q1 = q1(inputLines)
    print(f"Answer Q1: {result_q1}")
