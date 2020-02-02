import unittest
import asteroidMapping


class Test(unittest.TestCase):
    def test_1(self):
        filename = 'testInput.txt'
        expectedReturnValue = ((3, 4), 8)
        self.assertEqual(asteroidMapping.pickStation(filename),
                         expectedReturnValue)

    def test_2(self):
        filename = 'testInput2.txt'
        expectedReturnValue = ((5, 8), 33)
        self.assertEqual(asteroidMapping.pickStation(filename),
                         expectedReturnValue)

    def test_3(self):
        filename = 'testInput3.txt'
        expectedReturnValue = ((1, 2), 35)
        self.assertEqual(asteroidMapping.pickStation(filename),
                         expectedReturnValue)

    def test_4(self):
        filename = 'testInput4.txt'
        expectedReturnValue = ((6, 3), 41)
        self.assertEqual(asteroidMapping.pickStation(filename),
                         expectedReturnValue)

    def test_5(self):
        filename = 'testInput5.txt'
        expectedReturnValue = ((11, 13), 210)
        self.assertEqual(asteroidMapping.pickStation(filename),
                         expectedReturnValue)

    def test_6(self):
        filename = 'testInput6.txt'
        expectedReturnValue = (8, 3)
        self.assertEqual(asteroidMapping.pickStation(filename)[0],
                         expectedReturnValue)

    def test_5order(self):
        filename = 'testInput5.txt'
        result = asteroidMapping.destroyOrder(filename)
        self.assertEqual(len(result), 300)
        orderValues = [1, 2, 3, 10, 20, 50, 100, 199, 200, 201, 299]
        expectedReturnValues = [(11, 12), (12, 1), (12, 2), (12, 8), (16, 0),
                                (16, 9), (10, 16), (9, 6), (8, 2), (10, 9),
                                (11, 1)]
        for i, orderValue in enumerate(orderValues):
            self.assertEqual(result[orderValue], expectedReturnValues[i])

    def test_main1(self):
        filename = 'input.txt'
        expectedReturnValue = ((11, 19), 253)
        self.assertEqual(asteroidMapping.pickStation(filename),
                         expectedReturnValue)

    def test_main2(self):
        filename = 'input.txt'
        position = 200
        expectedReturnValue = (8, 15)
        self.assertEqual(asteroidMapping.destroyOrder(filename)[position],
                         expectedReturnValue)
