inputFile = open("Day2\inputFile.txt","r")
Lines = inputFile.readlines()

def probleme1(): 
    """
    Each line gives the password policy and then the password. 
    The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
    For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
    
    How many passwords are valid according to their policies?
    """

    countGoodPasswords = 0

    for line in Lines:
        currentInput = line.strip()
        currentInput = currentInput.split()
        
        occurenceToCount = currentInput[1][0]
        password = currentInput[2]
        counts = password.count(occurenceToCount)

        limits = currentInput[0].split("-")
        lowerLimit = int(limits[0])
        upperLimit = int(limits[1])
        if (counts >= lowerLimit and counts <= upperLimit):
            countGoodPasswords = countGoodPasswords +1
    
    print(countGoodPasswords)
        
def probleme2():
    """
    Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
    (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. 
    Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
    
    Given the same example list from above:
        1-3 a: abcde is valid: position 1 contains a and position 3 does not.
        1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
        2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
    
    How many passwords are valid according to the new interpretation of the policies?
    """

    countGoodPasswords = 0

    for line in Lines:
        currentInput = line.strip()
        currentInput = currentInput.split()
        
        occurenceToCount = currentInput[1][0]
        password = currentInput[2]

        limits = currentInput[0].split("-")
        index1 = int(limits[0])
        index2 = int(limits[1])
        print(index2)
        print(password)

        currentCount = 0

        if (occurenceToCount == password[index1-1]):
            currentCount = currentCount + 1
        
        if (occurenceToCount == password[index2-1]):
            currentCount = currentCount + 1

        if(currentCount == 1):
            countGoodPasswords = countGoodPasswords + 1 
    
    print(countGoodPasswords)

probleme2()