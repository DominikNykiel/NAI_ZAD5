def returnUnique(listOfLists, index):
    resultSet = set()
    for observationList in listOfLists:
        resultSet.add(observationList[index])

    return resultSet


def countUnique(listOfLists, index):
    return len(returnUnique(listOfLists, index))


def readFromFile(filepath):
    testList = []
    with open(filepath) as file_object:
        for line in file_object:
            testList.append(line.rstrip().split(';'))

    return testList


def getDictOfAtrributes(listofLists):
    dictOfAttributes = {}

    for attribute in returnUnique(listofLists, len(listofLists[0]) - 1):
        dictOfAttributes[attribute] = {"occurences": 0, "likelihood": 0}

        for attributeList in listofLists:
            if attributeList[len(attributeList) - 1] == attribute:
                dictOfAttributes[attribute]["occurences"] += 1

    return dictOfAttributes


def countAttributeWithDecision(listofLists, attributeToSearch, decisiveAttribute, currIndex):
    attCounter = 0
    for attributeVector in listofLists:
        if attributeVector[currIndex] == attributeToSearch and \
                attributeVector[len(attributeVector) - 1] == decisiveAttribute:
            attCounter += 1

    return attCounter
