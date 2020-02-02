import operator

incr = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}
ops = {1: operator.add, 2: operator.mul, 5: operator.truth, 6: operator.not_,
       7: operator.lt, 8: operator.eq}


class Intcode:
    def __init__(self, filename):
        with open(filename) as f:
            self.array = dict(
                enumerate([int(n) for n in (f.read().split(','))]))
        self.i = 0
        self.exitStatus = False
        self.relativeBase = 0

    def arrayGet(self, index):
        return self.array.get(index, 0)

    def processParameters(self, parameters, modes):
        result = []
        for index in range(len(parameters)):
            mode = modes % 10
            result.append(self.applyParameterMode(parameters[index], mode))
            modes //= 10
        return result

    def applyParameterMode(self, parameter, mode):
        switcher = {
            0: self.arrayGet(parameter),
            1: parameter,
            2: self.arrayGet(parameter + self.relativeBase)}
        return switcher.get(mode)

    def applyResultPosMode(self, resultPos, mode):
        switcher = {
            0: resultPos,
            2: resultPos + self.relativeBase}
        return switcher.get(mode)

    def operation(self, a, b, resultPos, opCode, modes):
        [a, b] = self.processParameters([a, b], modes)
        self.array[self.applyResultPosMode(resultPos, modes // 100)] = ops[
            opCode](a, b)

    def jump(self, cond, jump, opCode, modes):
        [cond, jump] = self.processParameters([cond, jump], modes)
        if ops[opCode](cond):
            self.i = jump - incr[opCode]

    def compute(self, inputs, returnValue):
        opCode = self.arrayGet(self.i) % 100
        modes = self.arrayGet(self.i) // 100
        a, b, c = self.arrayGet(self.i + 1), self.arrayGet(
            self.i + 2), self.arrayGet(self.i + 3)

        if opCode == 99:
            self.exitStatus = True
            return returnValue, True

        if opCode in [1, 2, 7, 8]:
            self.operation(a, b, c, opCode, modes)
        elif opCode == 3:
            try:
                self.array[self.applyResultPosMode(a, modes)] = next(inputs)
            except StopIteration:
                return returnValue, True
        elif opCode == 4:
            returnValue.append(self.applyParameterMode(a, modes))
        elif opCode in [5, 6]:
            self.jump(a, b, opCode, modes)
        elif opCode == 9:
            self.relativeBase += self.applyParameterMode(a, modes)
        self.i += incr[opCode]

        return returnValue, False

    def run(self, inputs):
        if self.exitStatus:
            return None
        inputs = iter([int(n) for n in inputs])
        breakStatus = False
        output = []
        count = 0
        while self.i < max(self.array.keys()) and not breakStatus:
            count += 1
            output, breakStatus = self.compute(inputs, output)
        if output == []:
            output = None
        return output
