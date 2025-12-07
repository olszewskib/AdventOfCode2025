import re

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def part_1(number: str) -> bool:
    regex = re.compile(r"^(.+)\1$")
    return bool(regex.match(number))

def part_2(number: str) -> bool:
    regex = re.compile(r"^(.+)\1+$")
    return bool(regex.match(number))


def main():
    data = read_file('./input.txt').splitlines()

    ranges = data[0].split(",")

    result = 0
    for r in ranges:
        lower = int(r.split("-")[0])
        upper = int(r.split("-")[1])

        for number in range(lower, upper + 1):
            if part_2(str(number)):
                result += number

    print(result)



if __name__ == "__main__":
    main()
