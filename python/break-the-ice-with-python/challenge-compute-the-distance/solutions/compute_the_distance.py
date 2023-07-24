import math


def compute_the_distance():
    x, y = 0, 0
    while True:
        s = input().split()
        if not s:
            break
        if s[0] == 'UP':                  # s[0] indicates command
            x -= int(s[1])                # s[1] indicates unit of move
        if s[0] == 'DOWN':
            x += int(s[1])
        if s[0] == 'LEFT':
            y -= int(s[1])
        if s[0] == 'RIGHT':
            y += int(s[1])
            # N**P means N^P
    # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
    dist = round(math.sqrt(x**2 + y**2))
    print(dist)


compute_the_distance()
