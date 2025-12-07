from collections import deque

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def get_beams(data: list[str]) -> tuple[list[list[str]],int]: 
    beams = [["."] * len(data[0]) for _ in range(len(data))]

    splits = 0
    for i in range(len(data) - 1):
        for j in range(len(data[0])):
            beams[i][j] = data[i][j] if beams[i][j] != "|" else "|"

            if data[i][j] == "S":
                beams[i+1][j] = "|"
                continue

            if beams[i][j] != "|":
                continue

            if data[i+1][j] == ".":
                beams[i+1][j] = "|"
                continue

            if data[i+1][j] == "^":
                beams[i+1][j-1] = "|"
                beams[i+1][j+1] = "|"
                splits += 1

    return (beams,splits)

def main():
    data = read_file('./test.txt').splitlines()

    beams, splits = get_beams(data)

    print(f"Part1: {splits}")

    for b in beams:
        print("".join(b))

    s = (1, data[0].index("S"))

    q = deque()
    q.appendleft(s)

    h = len(data)
    visited = set()
    paths = 0
    while len(q) > 0:
        v = q.pop()
        i, j = v

        if v in visited:
            paths -= 2
            continue

        print(f"({i},{j})")
        visited.add(v)

        while i < h:
            i += 1

            if i == h:
                break

            if data[i][j] == "^":
                q.appendleft((i, j-1))
                q.appendleft((i, j+1))
                paths *= 2
                break

    print(paths)





if __name__ == "__main__":
    main()
