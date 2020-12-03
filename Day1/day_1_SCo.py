inputFile = open("Day1\inputFile.txt","r")
Lines = inputFile.readlines()

def probleme1():
    """
    Find the two entries that sum to 2020; what do you get if you multiply them together?
    """
    for line in Lines:
        currentNum = line.strip()
        currentNum = int(currentNum)
        numWeAreLookingFor = 2020 - currentNum

        for line2 in Lines:
            newNum = line2.strip()
            newNum = int(newNum)
            if newNum == numWeAreLookingFor : 
                print(currentNum)









def probleme2helper(numWeAreLookingFor):
    """
    Find the two entries that sum to 2020; what do you get if you multiply them together?
    """
    for line in Lines:
        currentNum2 = line.strip()
        currentNum2 = int(currentNum2)

        for line2 in Lines:
            newNum = line2.strip()
            newNum = int(newNum)
            if numWeAreLookingFor == (newNum+currentNum2) : 
                print(newNum)




def probleme2():
    """
    In your expense report, what is the product of the three entries that sum to 2020?
    """
    for line in Lines:
        currentNum = line.strip()
        currentNum = int(currentNum)
        numWeAreLookingFor = 2020 - currentNum

        if probleme2helper(numWeAreLookingFor):
            print(currentNum)


probleme2()

