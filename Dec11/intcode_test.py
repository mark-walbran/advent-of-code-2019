import unittest
from dec11 import Intcode
from reference_intcode import Machine

DX = {0: 0, 1: 1, 2: 0, 3: -1}
DY = {0: 1, 1: 0, 2: -1, 3: 0}


class Test(unittest.TestCase):
    def test_expected_instructions(self):
        filename = 'input.txt'
        squares = {(0, 0): True}

        with open(filename) as f:
            array = [int(n) for n in (f.read().split(','))]
        machine = Machine(array)
        intcode = Intcode(filename)
        orientation = 0
        x = 0
        y = 0

        machine.run(squares[0, 0])
        expectedInstruction = machine.output(), machine.output()
        instruction = tuple(intcode.run([squares[0, 0]]))
        self.assertEqual(instruction, expectedInstruction)

        while not machine.halted():
            paint, turn = instruction
            squares[x, y] = paint
            orientation = (orientation + (1 if turn else -1)) % 4
            x += DX[orientation]
            y += DY[orientation]
            machine.run(squares[x, y] if (x, y) in squares else False)
            expectedInstruction = machine.output(), machine.output()
            instruction = tuple(
                intcode.run([squares[x, y] if (x, y) in squares else False]))
            self.assertEqual(instruction, expectedInstruction)
