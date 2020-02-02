from intcode import Intcode

DX = {0: 0, 1: 1, 2: 0, 3: -1}
DY = {0: 1, 1: 0, 2: -1, 3: 0}


def getInstruction(intcode, input):
    return intcode.compute([input])


def runRobot(filename, squares):
    intcode = Intcode(filename)
    orientation = 0  # 0 = up, 1 = right, 2 = down, 3 = left
    x = 0
    y = 0
    instruction = intcode.run([squares[0, 0]])

    while instruction:
        paint, turn = instruction
        squares[x, y] = paint
        orientation = (orientation + (1 if turn else -1)) % 4
        x += DX[orientation]
        y += DY[orientation]
        instruction = intcode.run(
                [squares[x, y] if (x, y) in squares else False])
    return squares


def getImage(filename):
    squares = runRobot(filename, {(0, 0): True})
    minX = min(squares)[0]
    maxX = max(squares)[0]
    minY = min(squares, key=lambda coord: coord[1])[1]
    maxY = max(squares, key=lambda coord: coord[1])[1]
    image = [['  '] * (maxX - minX + 1) for _ in range(maxY - minY + 1)]

    for (x, y), colour in squares.items():
        newY = -y
        newX = x - minX
        if colour == 1:
            image[newY][newX] = '██'
    return '\n'.join(''.join(row) for row in image)


def main():
    filename = 'input.txt'
    print(f"Part #1: Number of squares painted by robot when starting on a "
          f"black square: {len(runRobot(filename, {(0, 0): False}))}")

    print(f"Part #2: Number plate painted: \n{getImage(filename)}")


if __name__ == '__main__':
    main()
