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


if __name__ == "__main__":
    with open("Day12_RainRisk/Input.txt") as input:
        inputLines = [str(line.strip()) for line in input]

    # Q1
    positionNorthSouth = 0
    positionEastWest = 0
    currentDirection = "E"
    possibleDirections = ["E", "N", "W", "S"]
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

    print(f"Answer Q1: {abs(positionNorthSouth)+abs(positionEastWest)}")
