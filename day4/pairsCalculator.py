def contains_pairs(line_split):
    if line_split[1] >= line_split[2] and line_split[0] <= line_split[3]:
        return 1
    else:
        return 0


def fully_contained_pairs(line_split):
    if line_split[0] < line_split[2]:
        if line_split[1] >= line_split[3]:
            return 1
        else:
            return 0
    elif line_split[0] > line_split[2]:
        if line_split[1] <= line_split[3]:
            return 1
        else:
            return 0
    else:
        return 1
