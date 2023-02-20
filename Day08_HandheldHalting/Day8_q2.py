
inputFile = open(
    "/Users/samuelcordano/Documents/adventOfCode/Day8_HandheldHalting/Input.txt", "r")
Lines = inputFile.readlines()


def createArray():
    """
    Creating an Array of tuples where each row of the array is a tuple with (operation,argument,visited)
    """
    originalInputArray = []
    for line in Lines:
        currentInput = line.strip()
        currentOperation = currentInput.split(" ")[0]
        currentArgument = currentInput.split(" ")[1]
        originalInputArray.append((currentOperation, currentArgument, False))
    return originalInputArray


def applyIntruction(rowNum, accumulator, inputArray):
    rowNum = int(rowNum)
    if rowNum == 605:
        print(accumulator)
        return True
    operationAttribute = inputArray[rowNum][0]
    argumentAttribute = int(inputArray[rowNum][1])
    visitedAttribute = inputArray[rowNum][2]

    #print(f"rowNum: {rowNum} // inputArray[rowNum]: {inputArray[rowNum]} // accumulator: {accumulator}")

    if visitedAttribute == True:
        return False
    else:
        inputArray[rowNum] = (operationAttribute, argumentAttribute, True)
        if operationAttribute == "nop":
            return applyIntruction((rowNum+1), accumulator, inputArray)
        elif operationAttribute == "acc":
            return applyIntruction((rowNum+1), (accumulator+argumentAttribute), inputArray)
        elif operationAttribute == "jmp":
            return applyIntruction((rowNum+argumentAttribute), accumulator, inputArray)


def modifyArray(originalInputArray, rowToChange):
    rowToChange = int(rowToChange)
    operationAttribute = originalInputArray[rowToChange][0]
    argumentAttribute = originalInputArray[rowToChange][1]

    newArray = originalInputArray
    if operationAttribute == "nop":
        newArray[rowToChange] = ("jmp", argumentAttribute, False)
    elif operationAttribute == "jmp":
        newArray[rowToChange] = ("nop", argumentAttribute, False)
    return newArray


def q2():
    for currentRow in range(605):
        originalInputArray = createArray()
        newArray = modifyArray(originalInputArray, currentRow)
        if applyIntruction(0, 0, newArray):
            print(currentRow)
            print("currentRow")


createArray()
q2()
