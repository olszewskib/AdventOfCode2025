import pulp
from collections import deque

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def parse_line(line: str) -> tuple[int, list[list[int]], list[int]]:
    data = line.split(" ")

    pattern = data[0].strip('[]')
    pattern_mask = 0
    for i in range(len(pattern)):
        if pattern[i] == '#':
            pattern_mask = (pattern_mask | (1 << i))

    buttons = [button.strip('()').split(',') for button in data[1:-1]]

    b = []
    for button in buttons:
        b.append([int(x) for x in button])

    joltage = [int(j) for j in data[-1].strip('{}').split(',')]

    return (pattern_mask, b, joltage)

def apply_joltage(mask: int, joltage: str) -> tuple[bool, str]:
    j = [int(jolt) for jolt in joltage.split(",")]
    m = mask
    i = 0

    while m != 0:
        if (m & 1) == 1:
            j[i] -= 1
            if j[i] < 0:
                return (False, "")

        m = m >> 1
        i += 1

    return (True, ",".join([str(jolt) for jolt in j]))
        

def coin_change(result: int, masks: list[int], joltage: str) -> int:
    q = deque([(joltage,"-1")])
    empty = ("0," * len(joltage.split(","))).rstrip(",")

    dp = {}

    while len(q) > 0:
        current, prev = q.popleft()

        if dp.get(current) is not None:
            continue

        dp[current] = prev

        if current == empty:
            break

        for mask in masks:
            flag, jolt = apply_joltage(mask, current)
            if flag:
                q.append((jolt, current))

    presses = 0
    m = empty
    while(dp[m] != "-1"):
        m = dp[m]
        presses += 1

    return presses


def main():
    data = read_file('./input.txt').splitlines()
    result = 0

    for idx, line in enumerate(data):
        _, buttons, joltage = parse_line(line)

        p = pulp.LpProblem(f"MinButtonPresses_{idx}", pulp.LpMinimize)

        press_vars = [pulp.LpVariable(f'press_{i}', lowBound=0, cat='Integer') for i in range(len(buttons))]

        p += pulp.lpSum(press_vars)

        for j in range(len(joltage)):
            affected_vars = [press_vars[b] for b in range(len(buttons)) if j in buttons[b]]
            p += pulp.lpSum(affected_vars) == joltage[j]

        p.solve(pulp.PULP_CBC_CMD(msg=False))
        min_presses = int(pulp.value(p.objective))
        result += min_presses

    print(result)

if __name__ == "__main__":
    main()
