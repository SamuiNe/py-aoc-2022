file = open("input/adventOfCodeDay1Input.txt", "r")
currentFileReadline = file.readline()

elfCaloriesList : list[int] = []
currentElfCaloriesCount : int = 0

while currentFileReadline != '':
    if currentFileReadline != "\n":
        currentElfCaloriesCount += int(currentFileReadline)
    else:
        elfCaloriesList.append(currentElfCaloriesCount)
        currentElfCaloriesCount = 0

    currentFileReadline = file.readline()

# This is for making the list sorted by largest to smallest
elfCaloriesList.sort(reverse=True)

print("AoC 2022 Day 1 Part 1 Solution is", elfCaloriesList[0])
print(elfCaloriesList[:1])

print("AoC 2022 Day 1 Part 2 Solution is", sum(elfCaloriesList[:3]))
print(str(elfCaloriesList[:3]))
