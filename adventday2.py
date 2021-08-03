import re


def regexLine(line):
    x = re.findall("((\d)|(\d\d))-((\d)|(\d\d)) ([\w ]+): ([\w ]+)", line)
    # print(line)
    # print(x[0])
    return checkValidity(x[0][0], x[0][3], x[0][6], x[0][7])


def checkValidity(start, end, letter, line):
    print("{} to {} of {} in {}".format(start, end, letter, line))
    x = line.count(letter)
    print(x)
    if(x < int(start) or x > int(end)):
        return False
    else:
        return True


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
