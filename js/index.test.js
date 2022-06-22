import calculatePins from ".";

describe("PIN", () => {
  it("should calculate and order combinations when given one digit", () => {
    expect(calculatePins(1)).toEqual([1, 2, 4]);
  });
  it("should calculate and order combinations when given one digit on bottom row", () => {
    expect(calculatePins(9)).toEqual([8, 6, 9]);
  });
  it("should calculate combinations and order when given one digit on bottom row", () => {
    expect(calculatePins(8)).toEqual([5, 8, 7, 0, 9]);
  });
  it("should calculate combinations and order when given two digits", () => {
    expect(calculatePins(46)).toEqual([
      55, 15, 75, 45, 53, 13, 56, 16, 59, 19, 73, 43, 76, 46, 79, 49,
    ]);
  });
  it("should calculate all options and order when given numbers with more digits", () => {
    expect(calculatePins(97516).length).toBe(540);
  });
});
