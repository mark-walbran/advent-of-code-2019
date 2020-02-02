def parseData(data, width, height):
    layers = []
    i = 0
    while i < len(data):
        string = data[i: i + width * height]
        layers.append([int(char) for char in string])
        i += width * height
    return layers


def getCountInLayer(layer, number):
    count = 0
    for digit in layer:
        if digit == number:
            count += 1
    return count


def getMinZerosLayer(layers):
    numZeros = []
    for layer in layers:
        numZeros.append(getCountInLayer(layer, 0))
    return layers[numZeros.index(min(numZeros))]


def evaluateLayer(layer):
    return getCountInLayer(layer, 1) * getCountInLayer(layer, 2)


def getImage(filename):
    width = 25
    height = 6
    layers = parseData(open(filename).read(), width, height)
    result = [2] * width * height

    for layer in layers:
        for index, digit in enumerate(layer):
            if result[index] == 2 and digit != 2:
                result[index] = digit

    image = []
    for i in range(0, width * height, width):
        image.append(result[i:i + width])

    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            if pixel == 1:
                image[i][j] = '██'
            else:
                image[i][j] = '  '
    return '\n'.join(''.join(row) for row in image)


def main():
    filename = 'input.txt'
    width = 25
    height = 6
    layers = parseData(open(filename).read(), width, height)
    minZerosLayer = getMinZerosLayer(layers)
    result = evaluateLayer(minZerosLayer)
    print(f"Part #1: Layer with minimum number of zeros is: {minZerosLayer}")
    print(f"Number of 1 digits in this layer multiplied by the number of 2 digits is: {result}")

    print(f"Part #2: The message produced after decoding the image is: \n{getImage(filename)}")


if __name__ == '__main__':
    main()
