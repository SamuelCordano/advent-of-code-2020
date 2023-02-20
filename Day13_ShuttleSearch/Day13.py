def find_busID_leaving_sonnest(departTimestamp, busIDs):
    busID = 0
    minWaitTime = 100000
    for bus in busIDs:
        waitTime = bus - departTimestamp % bus
        if waitTime < minWaitTime:
            minWaitTime = waitTime
            busID = bus
    print(busID * minWaitTime)
    return (busID * minWaitTime)


if __name__ == "__main__":
    inputFile = open("Day13_ShuttleSearch/Input1.txt", "r")
    Lines = inputFile.readlines()

    input_list = []
    for line in Lines:
        currentInput = line.strip()
        input_list.append(currentInput)

    departTimestamp = int(input_list[0])
    busIDs = input_list[1].split(",")
    busIDs = [int(busID) for busID in busIDs if busID != "x"]
    print(busIDs)

    # Q1 - Find the bus that leaves the soonest
    find_busID_leaving_sonnest(departTimestamp, busIDs)
