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

    joltage = "0"
    for i in range(len(dp)):
        if joltage < bank[i]:
            joltage = bank[i]

        dp[i][1] = joltage

    for i in range(1, len(dp)):
        for j in range(2, SAFETY_OVERRIDE + 1):

            if j == (i + 1):
                dp[i][j] = dp[i-1][j-1] + bank[i]
                break

            if (dp[i-1][j-1] + bank[i]) > (dp[i-1][j]):
                dp[i][j] = (dp[i-1][j-1] + bank[i])
            else:
                dp[i][j] = dp[i-1][j]

    joltage = "0"

    for i in range(len(dp)):
        if dp[i][SAFETY_OVERRIDE] > joltage:
            joltage = dp[i][SAFETY_OVERRIDE]


    return int(joltage)


SAFETY_OVERRIDE = 12

def main():
    banks = read_file('./input.txt').splitlines()
    bank_len = len(banks[0])

    dp = [["0"] * (SAFETY_OVERRIDE + 1) for _ in range(bank_len)]

    total_joltage = 0

    for bank in banks:
        total_joltage += find_max_joltage_p2(bank,dp)

    print(total_joltage)


if __name__ == "__main__":
    main()
