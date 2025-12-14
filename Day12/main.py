from math import prod

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    data = read_file('./input.txt').splitlines()

    result = 0
    for line in data:
        l = line.split(": ")
        area = prod([ int(x) for x in l[0].split("x")])
        boxes = sum([ int(x) for x in l[1].split(" ")]) * 9
        if area >= boxes:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
