import pairsCalculator

file = open("input/adventOfCodeDay4Input.txt", "r")
currentFileReadline = file.readline()

fileStage1Split: list[str] = currentFileReadline.split(",")
fileStage2Split: list[list[int]] = [[], []]

fullyContainedPairsCount: int = 0
containsPairsCount: int = 0

while currentFileReadline != '':
    fileStage1Split: list[str] = currentFileReadline.split(",")
    fileStage2Split[0] = list(map(int, fileStage1Split[0].split("-")))
    fileStage2Split[1] = list(map(int, fileStage1Split[1].split("-")))

    containsPairsCount += pairsCalculator.contains_pairs(fileStage2Split)
    fullyContainedPairsCount += pairsCalculator.fully_contained_pairs(fileStage2Split)

    currentFileReadline = file.readline()

print("AoC 2022 Day 4 Part 1 Solution is", fullyContainedPairsCount)
print("AoC 2022 Day 4 Part 2 Solution is", containsPairsCount)
