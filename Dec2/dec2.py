def intcode(filename, noun, verb):
    with open(filename) as f:
        array = [int(x) for x in next(f).split(',')]
    array[1] = noun
    array[2] = verb

    i = 0;
    while i < len(array):
        if array[i] == 99:
            break

        a = array[array[i + 1]]
        b = array[array[i + 2]]
        resultIndex = array[i + 3]

        if array[i] == 1:
            array[resultIndex] = a + b
        elif array[i] == 2:
            array[resultIndex] = a * b

        i += 4

    return array

def findNounAndVerb(filename, desiredOutput):
    for noun in range(100):
        for verb in range(100):
            array = intcode(filename, noun, verb)

            if array[0] == desiredOutput:
                return noun, verb


def main():
    filename = 'input.txt'

    print(f"Part #1: The value at position 0 on program halt is {intcode(filename, 12, 2)[0]}")

    noun, verb = findNounAndVerb(filename, 19690720)
    print(f"Part #2: The noun: {noun}, verb: {verb} that cause the program to produce output 19690720.")
    print(f"100 * noun + verb = {100 * noun + verb}")


if __name__ == '__main__':
    main()
