def read_file(file_path) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def find_max_joltage_p1(bank: str) -> int:
    l: str = '0'
    r: str = '0'

    for i in range(len(bank) - 1):
        if bank[i] > l:
            l = bank[i]
            r = bank[i+1]

        if bank[i+1] > r:
            r = bank[i+1]

    return int(l + r)

def find_max_joltage_p2(bank: str, dp: list[list[str]]) -> int:
    safety_override = len(dp[0])

    joltage = "0"
    for i in range(len(dp)):
        joltage = max(joltage, bank[i])
        dp[i][1] = joltage

    max_joltage = "0"
    for i in range(1, len(dp)):
        for j in range(2, safety_override + 1):

            if j == (i + 1):
                dp[i][j] = dp[i-1][j-1] + bank[i]
                break

            if (dp[i-1][j-1] + bank[i]) > (dp[i-1][j]):
                dp[i][j] = (dp[i-1][j-1] + bank[i])
            else:
                dp[i][j] = dp[i-1][j]

            if j == safety_override:
                max_joltage = max(max_joltage, dp[i][j])

    return int(max_joltage)


SAFETY_OVERRIDE = 12

def main():
    banks = read_file('./input.txt').splitlines()
    bank_len = len(banks[0])

    dp = [["0"] * (SAFETY_OVERRIDE + 1) for _ in range(bank_len)]

    total_joltage = 0

    for bank in banks:
        total_joltage += find_max_joltage_p2(bank,dp)

    result = int(read_file('result.txt').rstrip())
    print(f"Correct: {total_joltage == result}")


if __name__ == "__main__":
    main()
