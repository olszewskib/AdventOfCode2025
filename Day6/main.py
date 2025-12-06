import re

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def parse_data_part1(data: list[str]) -> list[list[str]]:
    parsed_data = []

    for i in range(len(data) - 1):
        nums = re.compile('[1-9]+')
        parsed_data.append(nums.findall(data[i]))

    ops = re.compile('[*+]')
    parsed_data.append(ops.findall(data[-1]))

    return parsed_data

def parse_data_part2(data: list[str]) -> list[list[str]]:
    p = re.compile('[*+]')
    ops = p.findall(data[-1])
    op = 0

    parsed_data = [[] for _ in range(len(ops))]

    for c in range(len(data[0])):

        num = ""
        for r in range(len(data) - 1):
            if data[r][c] == " ":
                continue

            num += data[r][c]

        if num == "":
            op += 1
            continue

        parsed_data[op].append(num)

    for i in range(len(ops)):
        parsed_data[i].append(ops[i])

    return parsed_data



def grand_total_part1(data: list[list[str]]) -> int:
    grand_total = 0

    for col in range(len(data[0])):
        op = data[-1][col]

        result = int(data[0][col])
        for row in range(1, len(data) - 1):
            if op == '*':
                result *= int(data[row][col])
            elif op == '+':
                result += int(data[row][col])

        grand_total += result

    return grand_total

def grand_total_part2(data: list[list[str]]) -> int:
    grand_total = 0

    for row in range(len(data)):
        op = data[row][-1]

        result = int(data[row][0])
        for col in range(1, len(data[row]) - 1):
            if op == '*':
                result *= int(data[row][col])
            elif op == '+':
                result += int(data[row][col])

        grand_total += result

    return grand_total


def main():
    data = read_file('./input.txt').splitlines()
    data1 = parse_data_part1(data)
    data2 = parse_data_part2(data)

    print(f"Part1: {grand_total_part1(data1)}")
    print(f"Part2: {grand_total_part2(data2)}")

if __name__ == "__main__":
    main()
