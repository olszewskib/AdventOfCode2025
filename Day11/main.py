import math
from collections import deque

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def parse_data(data: list[str]) -> dict[str, list[str]]:
    graph = {}

    for line in data:
        l = line.split(" ")
        graph[l[0].rstrip(":")] = l[1:]

    graph["out"] = []
    return graph

def get_paths_count(g: dict[str, list[str]], start: str, target: str) -> int:
    memo = {}

    def count_paths(v):
        if v == target:
            return 1
        
        if v in memo:
            return memo[v]
        
        if v not in g:
            return 0

        total_paths = 0
        for u in g[v]:
            total_paths += count_paths(u)
        
        memo[v] = total_paths
        return total_paths

    return count_paths(start)


def main():
    data = read_file('./input.txt').splitlines()
    graph = parse_data(data)

    print(f"Part1: {get_paths_count(graph, "you", "out")}")

    paths = []
    paths.append(get_paths_count(graph, "svr", "fft"))
    paths.append(get_paths_count(graph, "fft", "dac"))
    paths.append(get_paths_count(graph, "dac", "out"))

    print(f"Part2: {math.prod(paths)}")


if __name__ == "__main__":
    main()

