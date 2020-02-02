DX = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
DY = {'U': 1, 'D': -1, 'L': 0, 'R': 0}


def getPoints(commands):
    x = 0;
    y = 0;
    length = 0;
    points = {}
    for cmd in commands:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U', 'D']
        for _ in range(n):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in points:
                points[(x, y)] = length
    return points


def main():
    filename = 'input.txt'
    A, B = open(filename).read().split('\n')
    A, B = [x.split(',') for x in [A, B]]

    pointsA = getPoints(A)
    pointsB = getPoints(B)

    intersections = pointsA.keys() & pointsB.keys()
    minManhattanDistance = min([abs(x) + abs(y) for (x, y) in intersections])
    minSteps = min([pointsA[p] + pointsB[p] for p in intersections])

    print(f"Intersections at {intersections}")
    print(f"Part #1: Minimum manhattan distance of an intersection is {minManhattanDistance}")
    print(f"Part #2: Minimum steps of an intersection is {minSteps}")


if __name__ == '__main__':
    main()
