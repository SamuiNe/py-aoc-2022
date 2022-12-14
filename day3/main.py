def calculate_priority(priority_letter):
    # From A being ASCII 65, (27 - 65 = -38)
    capital_letter_ascii_offset: int = -38

    # From a being ASCII 97, (1 - 97 = -96)
    lowercase_letter_ascii_offset: int = -96

    if priority_letter.isupper():
        return ord(priority_letter) + capital_letter_ascii_offset
    else:
        return ord(priority_letter) + lowercase_letter_ascii_offset


def clear_part2_sets(current_line_set):
    current_line_set[0].clear()
    current_line_set[1].clear()
    current_line_set[2].clear()

    return


file = open("input/adventOfCodeDay3Input.txt", "r")
currentFileReadline = file.readline()

currentPart1LineSet: set[str] = set()
currentPart2LineSet: list[set[str]] = [set(), set(), set()]

# From A being ASCII 65, (27 - 65 = -38)
CAPITAL_LETTER_ASCII_OFFSET: int = -38

# From a being ASCII 97, (1 - 97 = -96)
LOWERCASE_LETTER_ASCII_OFFSET: int = -96

compartmentLength: int = 0
compartmentHalfPoint: int = 0
compartmentPart1Index: int = 0
compartmentPart2Index: int = 0
compartmentLineIndex: int = 0
totalPart1Priority: int = 0
totalPart2Priority: int = 0
part1LineComplete: bool = 0

while currentFileReadline != '':
    # -1 offset since we do not count the \n.
    compartmentLength = len(currentFileReadline)
    compartmentLengthLineBreakExclusive = compartmentLength - 1
    compartmentHalfPoint = compartmentLength >> 1

    while compartmentPart1Index < compartmentHalfPoint:
        if currentFileReadline[compartmentPart1Index] not in currentPart2LineSet[compartmentPart2Index]:
            currentPart2LineSet[compartmentPart2Index].add(currentFileReadline[compartmentPart1Index])

        if currentFileReadline[compartmentPart1Index] not in currentPart1LineSet:
            currentPart1LineSet.add(currentFileReadline[compartmentPart1Index])

        compartmentPart1Index += 1

    while compartmentPart1Index < compartmentLengthLineBreakExclusive:
        if currentFileReadline[compartmentPart1Index] not in currentPart2LineSet[compartmentPart2Index]:
            currentPart2LineSet[compartmentPart2Index].add(currentFileReadline[compartmentPart1Index])

        if currentFileReadline[compartmentPart1Index] in currentPart1LineSet:
            totalPart1Priority += calculate_priority(currentFileReadline[compartmentPart1Index])
            break

        compartmentPart1Index += 1

    while compartmentPart1Index < compartmentLengthLineBreakExclusive:
        if currentFileReadline[compartmentPart1Index] not in currentPart2LineSet[compartmentPart2Index]:
            currentPart2LineSet[compartmentPart2Index].add(currentFileReadline[compartmentPart1Index])

        compartmentPart1Index += 1

    if compartmentPart2Index == 2:
        commonLetter = (set(currentPart2LineSet[0]).intersection(currentPart2LineSet[1])\
                        .intersection(currentPart2LineSet[2])).pop()
        totalPart2Priority += calculate_priority(commonLetter)
        clear_part2_sets(currentPart2LineSet)

    compartmentPart1Index = 0
    compartmentLineIndex += 1
    compartmentPart2Index = compartmentLineIndex % 3
    currentPart1LineSet.clear()
    currentFileReadline = file.readline()

print("AoC 2022 Day 3 Part 1 Solution is", totalPart1Priority)
print("AoC 2022 Day 3 Part 2 Solution is", totalPart2Priority)
file.close()
