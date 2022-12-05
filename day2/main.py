# Base score rewards: x = 1pt, y = 2pt, z = 3pt
# Result score rewards: Lose = 0pt, Draw = 3pt, Win = 6pt

scoreAwardsPart1 = {"A": {"X": 4, "Y": 8, "Z": 3},
                    "B": {"X": 1, "Y": 5, "Z": 9},
                    "C": {"X": 7, "Y": 2, "Z": 6}}

# Base score rewards: Rock = 1pt, Paper = 2pt, Scissors = 3pt
# Result score rewards: Lose = 0pt, Draw = 3pt, Win = 6pt
# For this part, X = Lose, Y = Draw, and Z = Win

scoreAwardsPart2 = {"A": {"X": 3, "Y": 4, "Z": 8},
                    "B": {"X": 1, "Y": 5, "Z": 9},
                    "C": {"X": 2, "Y": 6, "Z": 7}}

file = open("input/adventOfCodeDay2Input.txt", "r")
currentFileReadline = file.readline()

elfCaloriesList: list[int] = []
totalScorePart1: int = 0
totalScorePart2: int = 0

while currentFileReadline != '':
    currentFileReadlineArray: list[str] = currentFileReadline.split()
    totalScorePart1 += scoreAwardsPart1[currentFileReadlineArray[0]][currentFileReadlineArray[1]]
    totalScorePart2 += scoreAwardsPart2[currentFileReadlineArray[0]][currentFileReadlineArray[1]]

    currentFileReadline = file.readline()


print("AoC 2022 Day 2 Part 1 Solution is", totalScorePart1)
print("AoC 2022 Day 2 Part 2 Solution is", totalScorePart2)
