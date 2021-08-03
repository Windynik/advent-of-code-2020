import re


def regexLine(line):
    x = re.findall("((\d)|(\d\d))-((\d)|(\d\d)) ([\w ]+): ([\w ]+)", line)
    # return checkValidityPt1(x[0][0], x[0][3], x[0][6], x[0][7])
    return checkValidityPt2(x[0][0], x[0][3], x[0][6], x[0][7])


def checkValidityPt1(start, end, letter, line):
    print("{} to {} of {} in {}".format(start, end, letter, line))
    x = line.count(letter)
    print(x)
    if(x < int(start) or x > int(end)):
        return False
    else:
        return True


def checkValidityPt2(start, end, letter, line):
    x = 1 if line[int(start)-1] == letter else 0
    y = 1 if line[int(end)-1] == letter else 0
    if(x+y == 1):
        return True
    else:
        return False


fp = open("inputs/2.txt")
count = 0
messed_up = 0

while True:
    count += 1
    line = fp.readline()

    if not line:
        break
    if(regexLine(line.strip())):
        messed_up = messed_up+1
print(messed_up)
