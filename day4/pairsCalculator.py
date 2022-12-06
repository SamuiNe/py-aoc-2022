def contains_pairs(line_stage2_split):
    if line_stage2_split[0][1] >= line_stage2_split[1][0] and line_stage2_split[0][0] <= line_stage2_split[1][1]:
        return 1
    else:
        return 0


def fully_contained_pairs(line_stage2_split):
    if line_stage2_split[0][0] < line_stage2_split[1][0]:
        if line_stage2_split[0][1] >= line_stage2_split[1][1]:
            return 1
        else:
            return 0
    elif line_stage2_split[0][0] > line_stage2_split[1][0]:
        if line_stage2_split[0][1] <= line_stage2_split[1][1]:
            return 1
        else:
            return 0
    else:
        return 1
