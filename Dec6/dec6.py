class Node:
    def __init__(self):
        self.children = set()
        self.parent = None
        self.distance = None


def cumulativeDepth(node, depth):
    cDepth = 0
    for child in node.children:
        cDepth += cumulativeDepth(child, depth + 1)
    return cDepth + depth

def BFS(queue, end):
    node = queue.pop(0)
    for neighbour in (node.children.union({node.parent})):
        if neighbour == end:
            return node.distance + 1
        if neighbour != None and neighbour.distance == None:
            neighbour.distance = node.distance + 1
            queue.append(neighbour)


def calculation(filename):
    nodes = {'COM': Node()}
    with open(filename) as f:
        array = [tuple(a.split(')')) for a in f.read().split('\n')]

    for (parent, child) in array:
        if child not in nodes:
            nodes[child] = Node()
        if parent not in nodes:
            nodes[parent] = Node()

        nodes[parent].children.add(nodes[child])
        nodes[child].parent = nodes[parent]

    numOrbits = cumulativeDepth(nodes['COM'], 0)

    start = nodes['YOU'].parent
    start.distance = 0
    end = nodes['SAN'].parent
    queue = [start]

    while queue:
        santaDistance = BFS(queue, end)
        if santaDistance is not None:
            return numOrbits, santaDistance


def main():
    filename = 'input.txt'

    with open(filename) as f:
        array = [tuple(a.split(')')) for a in f.read().split('\n')]

    numOrbits, santaDistance = calculation(filename)
    print(f"Part #1: Total number of direct and indirect orbits in map: {numOrbits}")
    print(f"Part #2: Distance to Santa is: {santaDistance}")


if __name__ == '__main__':
    main()
