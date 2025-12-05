from bisect import bisect_left
from typing import Optional

def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def lower_bound(r: str) -> int:
    return int(r.split("-")[0])

def overlap(lower: str, upper: str) -> tuple[bool,Optional[str]]:
    l = lower.split("-")
    r = upper.split("-")

    if int(l[1]) >= int(r[0]):
        return (True,f"{l[0]}-{max(l[1],r[1])}")

    return (False, None)

def includes(r: str, x: str) -> bool:
    l,u = r.split("-")

    if int(l) <= int(x) and int(x) <= int(u):
        return True

    return False

def main():
    ranges = read_file('./ranges.txt').splitlines()
    ids = read_file('./ids.txt').splitlines()

    ranges.sort(reverse=True, key=lower_bound)
    ranges_merged = []

    while len(ranges) > 0:
        upper = ranges.pop()

        if len(ranges_merged) == 0:
            ranges_merged.append(upper)
            continue

        lower = ranges_merged.pop()

        flag, range_merged = overlap(lower,upper)

        if flag:
            ranges_merged.append(range_merged)
            continue

        ranges_merged.append(lower)
        ranges_merged.append(upper)
    

    result = 0
    for id in ids:
        index = bisect_left(ranges_merged, int(id), key=lower_bound) - 1

        if index < 0:
            continue

        if includes(ranges_merged[index],id):
            result += 1

        if index != (len(ranges_merged) - 1) and includes(ranges_merged[index+1],id):
            result += 1

    print(result)


if __name__ == "__main__":
    main()
