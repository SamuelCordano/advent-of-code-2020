inputFile = open("/Users/samuelcordano/Documents/adventOfCode/Day6_CustomCustoms/inputFile.txt","r")
Lines = inputFile.readlines()

def problem1():
    """
    For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
    """

    counter =0 #testing purposes
    currentGroupResponses = []
    sumCounts = 0

    for line in Lines: 
        #counter +=1
        currentInput = line.strip()
        currentInput = currentInput.split()

        if currentInput == []:
            #End of a group
            #check if all values are in the dictionnary, if so add 1 to count of good passports
            currentGroupResponses = [item for sublist in currentGroupResponses for item in sublist] #Flatten List of List
            currentGroupResponses = [item for sublist in currentGroupResponses for item in sublist] #Create List of characters
            currentGroupResponses = set(currentGroupResponses) #Create Set of characters, keeping
            sumCounts += len(currentGroupResponses)

            #Reset responses
            currentGroupResponses = []
        else: 
            currentGroupResponses.append(currentInput)
        
    print(sumCounts)
    return sumCounts


def problem2():
    """
    For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
    """

    counter =0 #testing purposes
    currentGroupResponses = []
    currentNumPeopleInGroup =0
    sumCounts = 0

    for line in Lines: 
        counter +=1
        currentInput = line.strip()
        currentInput = currentInput.split()
        
        if currentInput == []:
            #End of a group
            #check if all values are in the dictionnary, if so add 1 to count of good passports
            currentGroupResponses = [item for sublist in currentGroupResponses for item in sublist] #Flatten List of List
            currentGroupResponses = [item for sublist in currentGroupResponses for item in sublist] #Create List of characters
            currentGroupResponses = {x:currentGroupResponses.count(x) for x in currentGroupResponses} #Create Dict of characters, keeping

            
            # Iterate over all the items in dictionary and filter items 
            for (key, value) in currentGroupResponses.items():
                if value== currentNumPeopleInGroup:
                    sumCounts += 1

            #Reset responses
            currentGroupResponses = []
            currentNumPeopleInGroup =0
        else: 
            currentGroupResponses.append(currentInput)
            currentNumPeopleInGroup +=1
        
        #if counter== 10: return True

    print(sumCounts)
    return sumCounts
problem2()