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
        print(f"currentInput is: {currentInput}")
        currentBag = currentInput.split(" bags")[0]
        #currentBagName = currentBag.replace(" ", "_")

        currentChildBags = currentInput.split(" contain ",1)[1]
        currentChildBags = currentChildBags.replace(" bag.", " bags.")
        currentChildBags = currentChildBags.split(" bags.")[0]
        currentChildBags = currentChildBags.replace(" bag, ", " bags, ")
        currentChildBags = currentChildBags.split(" bags, ")
        currentChildBags = [element[2:] for element in currentChildBags]
        print(f"currentBag is: {currentBag}")
        print(f"childBags is: {currentChildBags}")
        
        if currentChildBags == [" other"]:
            currentChildBags = []
        print(f"childBags new is: {currentChildBags}")
        print(" ")

        #Create objectfor current bag if it doesn't exist: 
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


        #if counter ==10: 
        #    return True


listOfParentsShinyGold = []

def findAllParentBags(originalBag,listOfParentsShinyGold):
    print(originalBag)
    currentOriginalBagObject = listOfBags.get(originalBag)
    listOfParentBags = currentOriginalBagObject.parentBags

    for parentBag in listOfParentBags:
        currentParentBagObject = listOfBags.get(parentBag)
        if not currentParentBagObject.visited:
            currentParentBagObject.visited = True
            listOfParentsShinyGold += [parentBag]
            findAllParentBags(parentBag,listOfParentsShinyGold)

createGraph()
print("TESTING")

for individualBag in listOfBags: 
    currentBagObject = listOfBags.get(individualBag)
    print(currentBagObject)

findAllParentBags("shiny gold",listOfParentsShinyGold)
print(listOfParentsShinyGold)
print(len(listOfParentsShinyGold))

