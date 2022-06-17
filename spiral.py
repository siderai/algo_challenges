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


def can_move(sample, l, c, ld, cd):
    """
    Check whether can move in specified direction
    """
    # Move once
    l += ld
    c += cd

    # Sample is a square
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
    # Initial sample
    sample = [[0 for column in range(size)] for line in range(size)]

    # Create cursor to track line and column
    l = c = 0

    # Initial direction
    ld, cd = 0, 1

    # Draw a snake
    idle_turns = 0
    while idle_turns < 2:
        sample[l][c] = 1

        if can_move(sample, l, c, ld, cd):
            # Move
            l += ld
            c += cd
            idle_turns = 0
        else:
            # Turn clockwise:
            ld, cd = cd, -ld
            idle_turns += 1

    # Last step
    ld, cd = -cd, ld
    if sample[l + ld][c + cd] == 1:
        sample[l][c] = 0

    # Now sample is a spiral
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
