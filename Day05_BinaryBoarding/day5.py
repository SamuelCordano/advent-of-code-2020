inputFile = open("/Users/samuelcordano/Documents/adventOfCode/Day5_BinaryBoarding/inputFile.txt","r")
Lines = inputFile.readlines()

def problem2():
    """
    What is the ID of your seat?
    """

    listofIDs = []
    counter =0

    #Get list of IDs
    for line in Lines: 
        counter +=1
        currentInput = line.strip()
        rowMin = 0
        rowMax = 127
        seatMin = 0
        seatMax = 7
        print(currentInput)
        for element in currentInput:
            if element =="F":
                rowMax = rowMax - ((rowMax+1-rowMin)/2)
            elif element == "B":
                rowMin = rowMin + ((rowMax+1-rowMin)/2)
            elif element == "R":
                seatMin = seatMin + ((seatMax+1-seatMin)/2)
            elif element =="L":
                seatMax = seatMax - ((seatMax+1-seatMin)/2)
        id = rowMin *8 + seatMin
        listofIDs.append(id)

    #Find missing ID
    listofIDs.sort()
    for n in range(len(listofIDs)):
        idN =  int(listofIDs[n])
        idNplus1 =  int(listofIDs[n+1])
        if idNplus1-idN != 1:
            print("Here is my ID: " )
            print(idN+1)
            return idN +1

problem2()