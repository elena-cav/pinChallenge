from functools import reduce
from functools import cmp_to_key

pinPad = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [None, 0, None],
]
def findCombinations(list, n = 0, numbers = [], current = ''):
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
                    adjacent = pinPad[adjacentCol][adjacentRow]
                    return adjacent
    mapped = map(accessPinPad, [[-1, 0],[1, 0],[0, -1],[0, 1]])
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
 allCombinations = findCombinations(list(possiblePins))
 mostWorn = [5, 1, 2, 8, 7, 4, 0, 3, 6, 9]
#  print('allcomb', allCombinations)

 def letter_cmp(a, b):
    print('ab', a, b)
    splitA = list(str(a))
    splitB = list(str(b))
    def calculateIndex(pin):
        reduce(lambda a, b: mostWorn.index(int(a)) + mostWorn.index(int(b)), pin)
        aWorn = calculateIndex(splitA)
        bWorn = calculateIndex(splitB)
        print('splitab', splitA, splitB)
        print('HI',aWorn, bWorn)
        return aWorn - bWorn

 letter_cmp_key = cmp_to_key(letter_cmp)
 result = allCombinations.sort(key=letter_cmp_key)
#  print(result)








        
    


# print(list(possiblePins))

findPins(12)

