
inputFile = open(
    "/Users/samuelcordano/Documents/adventOfCode/Day8_HandheldHalting/Input.txt", "r")
Lines = inputFile.readlines()

inputArray = []


def createArray():
    """
    Creating an Array of tuples where each row of the array
    is a tuple with (operation,argument,visited)
    """
    for line in Lines:
        currentInput = line.strip()
        currentOperation = currentInput.split(" ")[0]
        currentArgument = currentInput.split(" ")[1]
        inputArray.append((currentOperation, currentArgument, False))


listInstructionsVisited = []


def applyIntruction(rowNum, accumulator):
    rowNum = int(rowNum)
    operationAttribute = inputArray[rowNum][0]
    argumentAttribute = int(inputArray[rowNum][1])
    visitedAttribute = inputArray[rowNum][2]

    print(
        f"rowNum: {rowNum} // inputArray[rowNum]: {inputArray[rowNum]} // accumulator: {accumulator}")

    if visitedAttribute:
        return accumulator
    else:
        inputArray[rowNum] = (operationAttribute, argumentAttribute, True)
        if operationAttribute == "nop":
            return applyIntruction((rowNum+1), accumulator)
        elif operationAttribute == "acc":
            return applyIntruction((rowNum+1), (accumulator+argumentAttribute))
        elif operationAttribute == "jmp":
            return applyIntruction((rowNum+argumentAttribute), accumulator)


createArray()
print(inputArray)

print(applyIntruction(0, 0))
