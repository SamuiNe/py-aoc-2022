import pairsCalculator
import re

file = open("input/adventOfCodeDay4Input.txt", "r")
currentFileReadline = file.readline()

lineSplit: list[int] = list(map(int, re.split(r'[-,]', currentFileReadline)))

fullyContainedPairsCount: int = 0
containsPairsCount: int = 0

while currentFileReadline != '':
    lineSplit = list(map(int, re.split(r'[-,]', currentFileReadline)))

    containsPairsCount += pairsCalculator.contains_pairs(lineSplit)
    fullyContainedPairsCount += pairsCalculator.fully_contained_pairs(lineSplit)

    currentFileReadline = file.readline()

print("AoC 2022 Day 4 Part 1 Solution is", fullyContainedPairsCount)
print("AoC 2022 Day 4 Part 2 Solution is", containsPairsCount)
file.close()