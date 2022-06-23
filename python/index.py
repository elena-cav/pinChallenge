pinPad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None],
]


def findCombinations(list, n=0, numbers=[], current=''):
    if (n == len(list)):
        numbers.append(int(current))
    else:
        for item in list[n]:
            findCombinations(list, n + 1, numbers, current + str(item))
    return numbers


def getAdjacentNumbers(rowIndex, columnIndex):
    def accessPinPad(item):
        if columnIndex is not None:
            adjacentCol = rowIndex + item[0]
            adjacentRow = columnIndex + item[1]
            if adjacentRow > -1 and adjacentCol > -1:
                adjacent = None
                try:
                    adjacent = pinPad[adjacentCol][adjacentRow]
                except IndexError:
                    print("Pinpad does not contain value")
                return adjacent
    mapped = map(accessPinPad, [[-1, 0], [1, 0], [0, -1], [0, 1]])
    filtered = filter(lambda item: item is not None, mapped)
    return list(filtered)


def findPins(pin):
    split = list(str(pin))
    possiblePins = list(map(lambda n: [int(n)], split))
    for i, num in enumerate(split):
        for rowIndex, row in enumerate(pinPad):
            integer = int(num)
            columnIndex = None
            try:
                columnIndex = row.index(integer)
            except ValueError:
                print("Row does not contain value")
            adjacentNumbers = getAdjacentNumbers(rowIndex, columnIndex)
            for j in adjacentNumbers:
                possiblePins[i].append(j)
    return findCombinations(list(possiblePins))


mostWorn = ['5', '1', '2', '8', '7', '4', '0', '3', '6', '9']


def generateDictionary(combinations):
    dictionaryOfProbability = {}
    for num in combinations:
        dictionaryOfProbability[num] = 0
        for num_smaller_than_9 in str(num):
            dictionaryOfProbability[num] += mostWorn.index(num_smaller_than_9)
    return dictionaryOfProbability


def generateResult(pin):
    combinations = findPins(pin)
    dictionaryOfProbability = generateDictionary(combinations)
    sort_orders = sorted(dictionaryOfProbability.items(), key=lambda x: x[1])
    result = []
    for i in sort_orders:
        result.append(i[0])
    print('RESULT:', result)
    print('RESULT length:', len(result))
    return result


generateResult(97516)
