def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def remove_tp(tp: list[list[str]]) -> int:
    n, m = len(tp), len(tp[0])

    dp = [[-1] * m for _ in range(n)]

    moves = [(1, -1), (1, 0), (1, 1), (0, 1)]

    for i in range(1, n + 1):
        ii = n - i
        for j in range(1, m + 1):
            jj = m - j

            if tp[ii][jj] != "@":
                continue
            else: 
                dp[ii][jj] = 0

            for move in moves:

                if ii + move[0] < 0 or ii + move[0] == n:
                    continue
                if jj + move[1] < 0 or jj + move[1] == m:
                    continue

                if tp[ii + move[0]][jj + move[1]] == "@":
                    dp[ii][jj] += 1
                    dp[ii + move[0]][jj + move[1]] += 1

    result = 0
    for i in range(n):
        for j in range(m):
            if dp[i][j] != -1 and dp[i][j] < 4:
                result += 1
                tp[i][j] = "."

    return result
    

def main():
    data = read_file('./input.txt').splitlines()

    tp = [list(line) for line in data]
    result = 0

    while True:
        removed = remove_tp(tp)
        if removed == 0:
            break

        result += removed

    print(result)



if __name__ == "__main__":
    main()
