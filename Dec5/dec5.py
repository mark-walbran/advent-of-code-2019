from intcode import Intcode


def main():
    filename = 'input.txt'

    intcode1 = Intcode(filename)
    intcode2 = Intcode(filename)
    print(f"Part #1: The diagnosic code output from the test diagnostic program: {intcode1.run([1])[-1]}")
    print(f"Part #2: The diagnosic code output from the thermal radiation controller: {intcode2.run([5])[0]}")


if __name__ == '__main__':
    main()
