file = open("input/adventOfCodeDay4Input.txt", "r")
currentFileReadline = file.readline()

fileStage1Split: list[str] = currentFileReadline.split(",")
fileStage2Split: list[list[int]] = [[], []]

fullyContainedPairs: int = 0

while currentFileReadline != '':
    fileStage1Split: list[str] = currentFileReadline.split(",")
    fileStage2Split[0] = list(map(int, fileStage1Split[0].split("-")))
    fileStage2Split[1] = list(map(int, fileStage1Split[1].split("-")))

    if fileStage2Split[0][0] < fileStage2Split[1][0]:
        if fileStage2Split[0][1] >= fileStage2Split[1][1]:
            fullyContainedPairs += 1
    elif fileStage2Split[0][0] > fileStage2Split[1][0]:
        if fileStage2Split[0][1] <= fileStage2Split[1][1]:
            fullyContainedPairs += 1
    else:
        fullyContainedPairs += 1

    currentFileReadline = file.readline()


# Not 519
print("AoC 2022 Day 4 Part 1 Solution is", fullyContainedPairs)
