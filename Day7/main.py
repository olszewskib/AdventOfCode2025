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

    q = deque()
    q.append(f"{data[0].index("S")}-{data[0].index("S")}")
    
    paths = set()
    h = len(data)

    realities = 0
    while len(q) > 0:
        p = q.pop()

        if p in paths:
            continue
        else:
            paths.add(p)

        path = p.split("-")
        i, j = len(path) - 1, int(path[-1])

        while i < h:
            i += 1

            if i == h:
                realities += 1
                break

            if data[i][j] == "^":
                q.appendleft(p + "-" + str(j+1))
                q.appendleft(p + "-" + str(j-1))
                break
            else:
                p = p + "-" + str(j)

    print(realities)





if __name__ == "__main__":
    main()
