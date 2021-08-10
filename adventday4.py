import re

fp = open("inputs/4.txt")
listText = []
stringText = ""
validPassports = 0


def parseFile(fp):
    tempList = []
    tempString = ""
    while True:
        line = fp.readline()
        if(line == "\n"):
            test = tempString.replace("\n", " ")
            tempList.append(test[:-1])
            tempString = ""

        else:
            tempString = tempString+line
        if not line:
            break
    return tempList


def parseString(listItem):
    global validPassports
    for i in listItem:
        splitList = i.split(" ")
        if checkValidity(splitList):
            validPassports += 1


def checkIfCIDExists(fieldItem):
    for i in fieldItem:
        if(i[0:3] == "cid"):
            return True

    return False


def checkValidity(fields):
    if len(fields) < 7:
        return False
    elif len(fields) == 7:
        if(checkIfCIDExists(fields)):
            return False
        else:
            print("\n{} {}".format(fields, checkIndividualFields(fields)))
            return checkIndividualFields(fields)
    elif len(fields) == 8:
        print("\n{} {}".format(fields, checkIndividualFields(fields)))
        return checkIndividualFields(fields)


def checkIndividualFields(field):
    for i in field:
        if(i[0:3] == "byr"):
            year = int(i[4:])
            if(year > 1919 and year < 2003):
                pass
            else:
                return False
        elif(i[0:3] == "iyr"):
            year = int(i[4:])
            if(year >= 2010 and year <= 2020):
                pass
            else:

                return False
        elif(i[0:3] == "eyr"):
            year = int(i[4:])
            if(year >= 2020 and year <= 2030):
                pass
            else:

                return False
        elif(i[0:3] == "pid"):
            value = i[4:]
            if(len(value) == 9):
                pass
            else:

                return False
        elif(i[0:3] == "ecl"):
            value = i[4:]
            if(value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                pass
            else:

                return False
        elif(i[0:3] == "hcl"):
            i[0] == "#" and set(i[1:]) <= set("0123456789abcdef"),

        elif(i[0:3] == "hgt"):
            value = i[4:]
            # print("{} {} {} ".format(value, value[:-2], value[-2:]))
            if(value[-2:] == "in"):
                val = int(value[:-2])
                if(val > 60 and val < 77):
                    pass
                else:

                    return False
            if(value[-2:] == "cm"):
                val = int(value[:-2])
                if(val >= 150 and val <= 193):
                    pass
                else:

                    return False
            elif value[-2:] not in ["cm", "in"]:
                return False
    return True


listText = parseFile(fp)
parseString(listText)
print(validPassports)
