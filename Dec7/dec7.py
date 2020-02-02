from intcode import Intcode
import itertools


def findThrusterSignal(filename, phaseSeq):
    phaseFlow = 0
    for phase in phaseSeq:
        intcode = Intcode(filename)
        phaseFlow = (intcode.run([phase, phaseFlow]))[0]
    return phaseFlow


def findFlowOnThrusterSignal(phaseSeq, filename):
    intcodes = [None] * len(phaseSeq)
    for i in range(len(phaseSeq)):
        intcodes[i] = Intcode(filename)
        intcodes[i].run([phaseSeq[i]])

    exitStatus = False
    phaseFlow = 0
    while not exitStatus:
        for i in range(len(intcodes)):
            output = intcodes[i].run([phaseFlow])
            if output is None:
                exitStatus = True
            else:
                phaseFlow = output[0]
    return phaseFlow


def part1(filename, phaseValues):
    phaseSeqPermutations = list(itertools.permutations(phaseValues))

    maxThrusterSignal = 0
    for phaseSeq in phaseSeqPermutations:
        thrusterSignal = findThrusterSignal(filename, phaseSeq)
        if thrusterSignal > maxThrusterSignal:
            maxThrusterSignal = thrusterSignal
            maxThrusterSignalPhaseSeq = phaseSeq
    return maxThrusterSignal, maxThrusterSignalPhaseSeq


def part2(filename, phaseValues):
    phaseSeqPermutations = list(itertools.permutations(phaseValues))

    maxThrusterSignal = 0
    for phaseSeq in phaseSeqPermutations:
        thrusterSignal = findFlowOnThrusterSignal(phaseSeq, filename)
        if thrusterSignal > maxThrusterSignal:
            maxThrusterSignal = thrusterSignal
            maxThrusterSignalPhaseSeq = phaseSeq

    return maxThrusterSignal, maxThrusterSignalPhaseSeq


def main():
    filename = 'input.txt'
    phaseValues1 = [0, 1, 2, 3, 4]
    phaseValues2 = [5, 6, 7, 8, 9]

    maxThrusterSignal1, maxThrusterSignalPhaseSeq1 = part1(filename, phaseValues1)
    maxThrusterSignal2, maxThrusterSignalPhaseSeq2 = part2(filename, phaseValues2)

    print(f"Part #1: Max thruster signal = {maxThrusterSignal1}")
    print(f"Phase setting sequence for this thrust = {maxThrusterSignalPhaseSeq1}")

    print(f"Part #2: Max thruster signal = {maxThrusterSignal2}")
    print(f"Phase setting sequence for this thrust = {maxThrusterSignalPhaseSeq2}")


if __name__ == '__main__':
    main()
