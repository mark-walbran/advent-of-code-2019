import unittest
from intcode import Intcode


class Test(unittest.TestCase):

    def test_1(self):
        filename = 'testInput.txt'
        intcode = Intcode(filename)
        userInput = []
        with open(filename) as f:
            expectedReturnValue = [int(n) for n in (f.read().split(','))]
        self.assertEqual(intcode.run(userInput), expectedReturnValue)

    def test_2(self):
        filename = 'testInput2.txt'
        intcode = Intcode(filename)
        userInput = []
        self.assertEqual(len(str(intcode.run(userInput)[0])), 16)

    def test_3(self):
        filename = 'testInput3.txt'
        intcode = Intcode(filename)
        userInput = []
        expectedReturnValue = [1125899906842624]
        self.assertEqual(intcode.run(userInput), expectedReturnValue)

    def test_main(self):
        filename = 'input.txt'
        intcode = Intcode(filename)
        userInput = [1]
        expectedReturnValue = [3335138414]
        result = intcode.run(userInput)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, expectedReturnValue)

    def test_main2(self):
        filename = 'input.txt'
        intcode = Intcode(filename)
        userInput = [2]
        expectedReturnValue = [49122]
        result = intcode.run(userInput)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, expectedReturnValue)
