def changeDirection(current_direction, instruction):
    change = int(int(instruction[1:]) / 90)
    if instruction[0] == "R":
        change = -change
    if current_direction == "N":
        possible_directions = ["N", "W", "S", "E"]
    elif current_direction == "S":
        possible_directions = ["S", "E", "N", "W"]
    elif current_direction == "E":
        possible_directions = ["E", "N", "W", "S"]
    elif current_direction == "W":
        possible_directions = ["W", "S", "E", "N"]
    return(possible_directions[change])


def change_waypoint_location(waypoint_north_south, waypoint_east_west, instruction):
    # Get Current Zone (ex: NorthWest: NW)
    if waypoint_north_south >= 0:
        current_waypoint_zone = "N"
    else:
        current_waypoint_zone = "S"
    if waypoint_east_west >= 0:
        current_waypoint_zone += "E"
    else:
        current_waypoint_zone += "W"

    change = int(int(instruction[1:]) / 90)
    if change == 2:
        return -waypoint_north_south, -waypoint_east_west
    elif (change == 3 and instruction[0] == "R") or (change == 1 and instruction[0] == "L"):
        return True
    elif (change == 3 and instruction[0] == "L") or (change == 1 and instruction[0] == "R"):
        return True

    # Get possible_directions
    if current_waypoint_zone == "NE":
        possible_directions = ["NE", "SE", "SW", "NW"]
    elif current_waypoint_zone == "SE":
        possible_directions = ["SE", "SW", "NW", "NE"]
    elif current_waypoint_zone == "SW":
        possible_directions = ["SW", "NW", "NE", "SE"]
    elif current_waypoint_zone == "NW":
        possible_directions = ["NW", "NE", "SE", "SW"]

    return False


def q1(inputLines):
    positionNorthSouth = 0
    positionEastWest = 0
    current_direction = "E"
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
            if current_direction == "N":
                positionNorthSouth += int(line[1:])
            elif current_direction == "S":
                positionNorthSouth -= int(line[1:])
            elif current_direction == "E":
                positionEastWest += int(line[1:])
            elif current_direction == "W":
                positionEastWest -= int(line[1:])
        elif line[0] == "L" or line[0] == "R":
            current_direction = changeDirection(current_direction, line)

    return(abs(positionNorthSouth)+abs(positionEastWest))


def q2(inputLines):
    positionNorthSouth = 0
    positionEastWest = 0
    waypoint_north_south = 1
    waypoint_east_west = 10
    current_direction = "E"
    for line in inputLines:
        if line[0] == "N":
            waypoint_north_south += int(line[1:])
        elif line[0] == "S":
            waypoint_north_south -= int(line[1:])
        elif line[0] == "E":
            waypoint_east_west += int(line[1:])
        elif line[0] == "W":
            waypoint_east_west -= int(line[1:])
        elif line[0] == "F":
            positionNorthSouth += int(line[1:]) * waypoint_north_south
            positionEastWest += int(line[1:]) * waypoint_east_west
        elif line[0] == "L" or line[0] == "R":
            waypoint_north_south, waypoint_east_west = change_waypoint_location(
                waypoint_north_south, waypoint_east_west, line)

    return(abs(positionNorthSouth)+abs(positionEastWest))


if __name__ == "__main__":
    with open("Day12_RainRisk/Input.txt") as input:
        inputLines = [str(line.strip()) for line in input]

    result_q1 = q1(inputLines)
    print(f"Answer Q1: {result_q1}")
