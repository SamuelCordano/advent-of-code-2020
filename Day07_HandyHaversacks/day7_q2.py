import math

inputFile = open("/Users/samuelcordano/Documents/adventOfCode/Day7_HandyHaversacks/inputFile.txt","r")
Lines = inputFile.readlines()

class bag: 

    def __init__(self,name,childBags,parentBags) -> None:
        self.name = name
        self.childBags= childBags
        self.parentBags = parentBags
        self.visited = False

    def __str__(self):
        #print(f"name: {self.name} | childBags: {self.childBags}| parentBags: {self.parentBags}| visited: {self.visited}")
        return(f"name: {self.name} | childBags: {self.childBags}| parentBags: {self.parentBags}| visited: {self.visited}")

listOfBags = {}


def createGraph():
    """
    For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
    """

    counter =0 #testing purposes

    for line in Lines: 
        counter +=1
        currentInput = line.strip()
        
        #Clean Inputs
        #print(f"currentInput is: {currentInput}")
        currentBag = currentInput.split(" bags")[0]
        #currentBagName = currentBag.replace(" ", "_")

        currentChildBags = currentInput.split(" contain ",1)[1]
        currentChildBags = currentChildBags.replace(" bag.", " bags.")
        currentChildBags = currentChildBags.split(" bags.")[0]
        currentChildBags = currentChildBags.replace(" bag, ", " bags, ")
        currentChildBags = currentChildBags.split(" bags, ")
        #print(f"childBags is: {currentChildBags}")

        if currentChildBags == ['no other']: 
            currentChildBags = []
        else: 
            currentChildBagsNumbers = [int(element[0]) for element in currentChildBags]
            currentChildBagsNames = [element[2:] for element in currentChildBags]
            currentChildBags = list(zip(currentChildBagsNames,currentChildBagsNumbers))

        #print(f"currentBag is: {currentBag}")
        #print(f"childBags is: {currentChildBags}")
        #print(f"  ")
        #Create object for current bag if it doesn't exist: 
        if currentBag in listOfBags: 
            currentBagObject = listOfBags.get(currentBag)
            currentBagObject.childBags = currentChildBags
        else: 
            listOfBags[currentBag] = bag(currentBag,currentChildBags,[])
        
        #For each childbag, create an object if it isn't done and add current bag as a parentbag
        for childBag in currentChildBags: 
            if childBag not in listOfBags:
                listOfBags[childBag] = bag(childBag,[],[currentBag])

            else: 
                currentChildBagObject = listOfBags.get(childBag)
                currentChildBagObject.parentBags = currentChildBagObject.parentBags + [currentBag]


        #if counter ==3: 
        #    return True


numberOfBagsContained = []

def findAllBagsContained(originalBag):
    
    currentOriginalBagObject = listOfBags.get(originalBag)
    listOfChildBags = currentOriginalBagObject.childBags
    
    if listOfChildBags == []:
        #numberOfBagsContained.append(1)
        print(f"The originalBag is: {originalBag}. His Child Bags are: {listOfChildBags}")
        print(f" ")
        return 0
    else:
        resultArray = []
        for childBags in listOfChildBags:
            resultArray.append((int(childBags[1]) + (int(childBags[1])*int(findAllBagsContained(childBags[0])))))
        
        result = sum(resultArray)
        print(f"The originalBag is: {originalBag}. His Child Bags are: {listOfChildBags}")
        print(f"Number of bags in 1 {originalBag} is: {result}.")
        print(f"resultArray: {resultArray}")
        print(f" ")

        return result

createGraph()
print("TESTING")

#for individualBag in listOfBags: 
#    currentBagObject = listOfBags.get(individualBag)
#    print(currentBagObject)


finalResult = findAllBagsContained("shiny gold")
print(f"finalResult is: {finalResult}")


testResult = 1
for x in numberOfBagsContained:
    x = int(x)
    testResult = testResult * x

print(f"testResult is: {testResult}")
