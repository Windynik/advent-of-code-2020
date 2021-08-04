import re

inputsforPt1 = [1, 2]
inputsforPt2 = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def checkTrees(line, inputs):
    try:
        if(line[inputs[0]] == "#"):
            return 1
        else:
            return 0
    except Exception as e:
        pass


def treeTobogganing(inputs, fp):
    # global inputsforPt1
    positionInput = inputs
    count = 0
    trees = 0
    while True:
        line = fp.readline()

        if not line:
            break
        x = checkTrees(
            line, positionInput) if count == positionInput[1] else None
        positionInput = [(positionInput[0]+inputs[0]) % 31, positionInput[1] +
                         inputs[1]] if x == 1 or x == 0 else [positionInput[0], positionInput[1]]
        trees = trees + (x if x is not None else 0)
        count += 1
    return trees


def pt1():
    fp = open("inputs/3.txt")
    trees = treeTobogganing(inputsforPt1, fp)
    print("The answer for part 1 : {}".format(trees))


def pt2():
    trees = 1
    for inputs in inputsforPt2:
        fp = open("inputs/3.txt")
        trees = trees*treeTobogganing(inputs, fp)
    print("The answer for part 1 : {}".format(trees))


pt1()
pt2()
