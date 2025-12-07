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
    data = read_file('./input.txt').splitlines()

    beams, splits = get_beams(data)

    dp = [[0] * len(data[0]) for _ in range(len(data))]

    dp[0][data[0].index("S")] = 1

    for i in range(1, len(data)):
        for j in range(len(data[0])):

            if beams[i][j] == "^":
                dp[i][j-1] += dp[i-1][j]
                dp[i][j+1] += dp[i-1][j]
            elif beams[i][j] == "|":
                dp[i][j] += dp[i-1][j]

    realities = sum(dp[-1])

    print(f"Part1: {splits}")
    print(f"Part2: {realities}")


if __name__ == "__main__":
    main()
