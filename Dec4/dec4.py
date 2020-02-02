def part1(lowerLimit, upperLimit):
    validNumbers = set()
    for i in range(lowerLimit, upperLimit + 1):
        iString = str(i)
        prevC = 0
        flag1 = False
        flag2 = True
        for c in iString:
            if c == prevC:
                flag1 = True
            if int(c) < int(prevC):
                flag2 = False
            prevC = c

        if flag1 and flag2:
            validNumbers.add(i)
    return len(validNumbers)


def part2(lowerLimit, upperLimit):
    validNumbers = set()

    for i in range(lowerLimit, upperLimit + 1):
        iString = str(i)
        prevC = iString[0]
        flag1 = False
        flag2 = True
        for j in range(1, len(iString)):
            c = iString[j]
            if c == prevC and (
                    j == len(iString) - 1 or iString[j + 1] != c) and (
                    j == 1 or iString[j - 2] != c):
                flag1 = True
            if int(c) < int(prevC):
                flag2 = False
            prevC = c

        if flag1 and flag2:
            validNumbers.add(i)

    return len(validNumbers)


def main():
    lowerLimit = 183564
    upperLimit = 657474

    print(f"Part #1: The number of different passwords within the range given that meet the criteria: {part1(lowerLimit, upperLimit)}")
    print(f"Part #2: The number of different passwords within the range given that meet the updated criteria: {part2(lowerLimit, upperLimit)}")


if __name__ == '__main__':
    main()
