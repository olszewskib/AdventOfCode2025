import numpy as np
import heapq as hq
import math

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def norm(p1: str, p2: str):
    v1 = np.array([int(num) for num in p1.split(",")])
    v2 = np.array([int(num) for num in p2.split(",")])

    return np.linalg.norm(v1 - v2)

class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, v):
        if v not in self.parent:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if v not in self.parent:
            self.add(v)

        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)

        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


CIRCUITS_LIMIT = 1000

def main():
    data = read_file('./input.txt').splitlines()

    boxes = []
    for i in range(len(data)):
        p1 = data[i]
        for j in range(i + 1, len(data)):
            p2 = data[j]

            distance = norm(p1, p2)
            boxes.append((distance, p1, p2))
    boxes.sort()

    dsu = DSU()

    for b in boxes[:CIRCUITS_LIMIT]:
        _, v, u = b
        dsu.union(v, u)

    circuits = {}
    for k in dsu.parent.keys():
        p = dsu.find(k)

        if p not in circuits:
            circuits[p] = 1
        else:
            circuits[p] += 1

    lens = [v for _, v in circuits.items()]
    lens.sort()
    print(math.prod(lens[-3:]))


if __name__ == "__main__":
    main()
