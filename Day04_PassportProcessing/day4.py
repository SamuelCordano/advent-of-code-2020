import re

inputFile = open("inputFile.txt","r")
Lines = inputFile.readlines()

def checkYear(year,min,max):
    if year >= min and year <=max:
        return True
    else: 
        return False

def checkHeight(height):
    metricSystem = height[-2:]
    actualHeight = height
    if metricSystem == "cm":
        actualHeight = (height[0:3])
        if actualHeight.isnumeric():
            actualHeight = int(actualHeight)
            if  actualHeight >=150 and actualHeight<=193:
                return True
    elif metricSystem == "in":
        actualHeight = (height[0:2])
        if actualHeight.isnumeric():
            actualHeight = int(actualHeight)
            if actualHeight >=59 and actualHeight<=76:
                return True
    return False

def checkEyeColor(eyeColor):
    if eyeColor in ["amb","blu","brn","gry","grn","hzl","oth"]:
        return True
    else: 
        return False

def checkPassportId(passportId):
    if len(passportId)==9 and passportId.isnumeric():
        return True
    else:
        return False

def checkHairColor(hairColor):
    if hairColor[0] == "#" and len(hairColor)==7:
        hairColor = hairColor[1:]

        p = re.compile("[a-f0-9]{6,6}")
        m = p.match(hairColor)
        if m:
            return True
        else:
            return False
    else: 
        return False

def problem1():
    """
    Count the number of valid passports - those that have all required fields. 
    Treat cid as optional. In your batch file, how many passports are valid?
    """

    numberCorrectPassport = 0
    counter =0 #testing purposes
    fieldsCurrentPassport = []

    for line in Lines:
        #counter += 1  #testing purposes

        currentInput = line.strip()
        currentInput = currentInput.split()

        if currentInput == []:
            #End of a Passport
            #check if all values are in the dictionnary, if so add 1 to count of good passports
            fieldsCurrentPassport.sort()
            if fieldsCurrentPassport == ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'] or fieldsCurrentPassport ==['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']:
                numberCorrectPassport +=1
                print(fieldsCurrentPassport)
                print("Correct passport :) ")
            fieldsCurrentPassport = [] #clear dictionnary


        transformedInput = [element[0:3] for element in currentInput]
        print(transformedInput)

        fieldsCurrentPassport = fieldsCurrentPassport +(transformedInput)
        print(fieldsCurrentPassport)
        

        if counter > 17: return numberCorrectPassport #testing purposes
    return numberCorrectPassport

def problem2():
    """
    Count the number of valid passports - those that have all required fields and valid values. 
    Continue to treat cid as optional. In your batch file, how many passports are valid?
    """

    numberCorrectPassport = 0
    counter =0 #testing purposes
    fieldsCurrentPassport = {}

    for line in Lines:
        #counter += 1  #testing purposes

        currentInput = line.strip()
        currentInput = currentInput.split()

        if currentInput == []:
            #End of a Passport
            #Check 1: check if all fileds are in the dictionnary
            print(fieldsCurrentPassport)
            keys = sorted(fieldsCurrentPassport.keys())
            if keys == ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'] or keys ==['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']:
                print("check 1 validated")
                #Check 2: check if all fields respect rules:
                birthYear = int(fieldsCurrentPassport.get("byr"))
                issueYear = int(fieldsCurrentPassport.get("iyr"))
                expirationYear = int(fieldsCurrentPassport.get("eyr"))
                print("expirationYear is "+ str(expirationYear))
                print(checkYear(expirationYear,2020,2030))
                height = fieldsCurrentPassport.get("hgt")
                print("Height is "+ height)
                print(checkHeight(height))
                hairColor = fieldsCurrentPassport.get("hcl")
                print("Hair color is "+ hairColor)
                print(checkHairColor(hairColor))
                eyeColor = fieldsCurrentPassport.get("ecl")
                print("Eye color is "+ eyeColor)
                print(checkEyeColor(eyeColor))
                passportId= fieldsCurrentPassport.get("pid")
                print("passportId is "+ passportId)
                print(checkPassportId(passportId))
                
                if checkHairColor(hairColor) and checkHeight(height) and checkEyeColor(eyeColor) and checkPassportId(passportId) and \
                    checkYear(birthYear,1920,2002) and checkYear(issueYear,2010,2020) and checkYear(expirationYear,2020,2030): 
                    numberCorrectPassport +=1
            fieldsCurrentPassport = {}


        else: 
            for element in currentInput:
                currentKey = element[0:3]
                currentvalue =element[4:]
                fieldsCurrentPassport[currentKey] = currentvalue
            

        if counter > 17: 
            return numberCorrectPassport #testing purposes
    return numberCorrectPassport

#resultat = str(problem1())
#print(f"Number of correct passports: {resultat}")

resultat2 = str(problem2())
print(resultat2)
print(f"Number of passports with all fields present and valid: {resultat2}")

#test_list = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
#print(test_list)
#test_list_sorted = test_list.sort()
#print(test_list)

#resulttest = checkEyeColor("#aaa")
#print(resulttest) 

