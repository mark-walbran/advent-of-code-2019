from intcode import Intcode

def main():
    filename = 'input.txt'
    intcode1 = Intcode(filename)
    intcode2 = Intcode(filename)
    print(f"Part #1: Boost keycode = {intcode1.run([1])[0]}")
    print(f"Part #2: Distress signal co-ordinates = {intcode2.run([2])[0]}")


if __name__ == '__main__':
    main()
