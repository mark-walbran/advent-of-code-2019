import math
from collections import OrderedDict


def loadCoords(filename):
    with open(filename, 'r') as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, c in enumerate(line):
                if c == '#':
                    yield (x, y)


def getAngle(start, end):
    return (math.atan2(end[0] - start[0], start[1] - end[1])) * (
                180 / math.pi) % 360


def pickStation(filename):
    coords = list(loadCoords(filename))
    asteroidScores = {}
    for start in coords:
        asteroidScores[start] = len(
                {getAngle(start, end) for end in coords if start != end})
    maximum = max(asteroidScores, key=asteroidScores.get)
    return maximum, asteroidScores[maximum]


def getSortedAsteroids(filename, start):
    coords = list(loadCoords(filename))
    coords.remove(start)
    sortedAsteroids = {}
    for end in coords:
        sortedAsteroids.setdefault(getAngle(start, end), []).append(end)
    for line in sortedAsteroids.values():
        line.sort(key=lambda val: math.sqrt(
            math.pow(val[0] - start[0], 2) + math.pow(val[1] - start[1], 2)))
    return OrderedDict(sorted(sortedAsteroids.items()))


def destroyOrder(filename):
    start, _ = pickStation(filename)
    sortedAsteroids = getSortedAsteroids(filename, start)
    asteroidOrder = [start]
    while sortedAsteroids:
        newSortedAsteroids = OrderedDict()
        for key, value in sortedAsteroids.items():
            asteroidOrder.append(value.pop(0))
            if value:
                newSortedAsteroids[key] = value
        sortedAsteroids = newSortedAsteroids
    return asteroidOrder


def main():
    filename = 'input.txt'
    result = pickStation(filename)
    print(
        f"Part #1: The co-ordinates of the best asteroid to have the base on are {result[0]}, which can monitor {result[1]} asteroids")
    position = 200
    result = destroyOrder(filename)[position]
    print(
        f"Part #2: Asteroid #{position} to be vaporised is: {result} which gives it a value of: {100 * result[0] + result[1]}")


if __name__ == '__main__':
    main()
