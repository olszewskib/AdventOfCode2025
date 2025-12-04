def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def parse_sequence(seq: str) -> int:
    direction = 1 if seq[0] == "R" else -1
    return int(seq[1:]) * direction

def part_1(data: list[str], starting_position: int) -> int:
    position = starting_position

    password = 0
    for rotation in data:

        position += parse_sequence(rotation)

        position = position % 100

        if position == 0:
            password += 1

    return password

def part_2(data: list[str], starting_position: int) -> int:
    position = starting_position

    password = 0
    for sequence in data:
        rotation = parse_sequence(sequence)

        r = abs(rotation)
        password += r // 100

        sgn = rotation // r
        rotation = sgn * (r % 100)
        new_position = position + rotation

        if new_position % 100 == 0:
            password += 1
            position = new_position % 100
            continue

        if position != 0 and new_position % 100 != new_position:
            password += 1
            position = new_position % 100
            continue

        position = new_position % 100

    return password

def main():
    data = read_file('./input.txt').splitlines()
    starting_position = 50

    result_1 = part_1(data, starting_position)
    print(f"Part1: {result_1}")

    starting_position = 50
    result_2 = part_2(data, starting_position)
    print(f"Part2: {result_2}")

if __name__ == "__main__":
    main()
