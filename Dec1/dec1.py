def fuelRequired(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + fuelRequired(fuel)


def part1(filename):
    with open(filename) as f:
        array = [int(n) for n in f.read().split('\n') if n.isdigit()]

    sum = 0;
    for value in array:
        sum += int(value) // 3 - 2

    return sum

def part2(filename):
    with open(filename) as f:
        array = [int(n) for n in f.read().split('\n') if n.isdigit()]

    sum = 0
    for value in array:
        sum += fuelRequired(value)

    return sum


def main():
    filename = 'input.txt'

    print(f"Part #1: Sum of fuel requirements for all modules: {part1(filename)}")
    print(f"Part #2: Sum of fuel requirements for all modules when also taking into account mass of fuel: {part2(filename)}")


if __name__ == '__main__':
    main()
