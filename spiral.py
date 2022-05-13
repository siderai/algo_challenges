# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
# Make a spiral

# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000

# Spiralize(5) should return this:
# [[1,1,1,1,1],
# [0,0,0,0,1],
# [1,1,1,0,1],
# [1,0,0,0,1],
# [1,1,1,1,1]]

def can_move(sample, l, c, ld, cd):
    """
    Check whether can move in specified direction
    """
    # Move once
    l += ld
    c += cd

    # sample is a square
    length = len(sample)

    # Cannot move outside of minimap
    if l < 0 or l >= length or c < 0 or c >= length:
        return False

    # Cannot move if occupied
    if sample[l][c] == 1:
        return False

    # Move second time
    l += ld
    c += cd

    # Can move if second move falls outside
    if l < 0 or l >= length or c < 0 or c >= length:
        return True

    # Cannot move if second move is occupied
    if sample[l][c] == 1:
        return False

    # Otherwise we can move
    return True


def spiralize(size):
    # initial sample
    sample = [[0 for line in range(size)] for column in range(size)]

    # create cursor to track line and column
    l = c = 0

    # initial direction
    ld, cd = 0, 1

    # draw a snake
    idle_turns = 0
    while idle_turns < 2:
        sample[l][c] = 1

        if can_move(sample, l, c, ld, cd):
            # move
            l += ld
            c += cd
            idle_turns = 0
        else:
            # turn clockwise:
            ld, cd = cd, -ld
            idle_turns += 1

    # Last step
    ld, cd = -cd, ld
    if sample[l + ld][c + cd] == 1:
        sample[l][c] = 0

    # now sample is a spiral
    spiral = sample
    return spiral


assert spiralize(5) == [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

assert spiralize(9) == [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]
