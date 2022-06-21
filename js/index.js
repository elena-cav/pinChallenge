const pinPad = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [null, 0, null],
];

const findCombinations = (list, n = 0, numbers = [], current = "") => {
  if (n === list.length) {
    numbers.push(Number(current));
  } else
    list[n].forEach((item) => {
      return findCombinations(list, n + 1, numbers, current + item);
    });
  return numbers;
};
// [[1, 2, 3], [2]];
const splitPin = (pin) => pin.toString().split("");

const getAdjacentNumbers = (rowIndex, columnIndex) => {
  return [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ]
    .map(([r, c]) => {
      return pinPad[rowIndex + r]?.[columnIndex + c];
    })
    .filter((item) => typeof item === "number");
};

export default (pin) => {
  const split = splitPin(pin);

  const possiblePins = split.map((n) => [Number(n)]);

  split.forEach((num, i) => {
    pinPad.forEach((row, rowIndex) => {
      const int = Number(num);
      const columnIndex = row.indexOf(int);
      if (columnIndex !== -1) {
        const adjacentNumbers = getAdjacentNumbers(rowIndex, columnIndex);
        for (let j = 0; j < adjacentNumbers.length; j++) {
          possiblePins[i].push(adjacentNumbers[j]);
        }
      }
    });
  });
  const mostWorn = [5, 1, 2, 8, 7, 4, 0, 3, 6, 9];
  const result = findCombinations(possiblePins).sort((a, b) => {
    const splitA = splitPin(a);
    const splitB = splitPin(b);
    const calculateIndex = (pin) =>
      pin.reduce((acc, item) => {
        return acc + mostWorn.indexOf(Number(item));
      }, 0);
    const aWorn = calculateIndex(splitA);
    const bWorn = calculateIndex(splitB);
    return aWorn - bWorn;
  });
  return result;
};
