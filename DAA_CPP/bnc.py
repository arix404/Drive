
n = int(input("Enter n: "))
r = int(input("Enter r: "))

if r < 0 or r > n:
    print("Invalid input")

else:
    dp = [[0] * (r + 1) for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, r) + 1):

            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    print("Binomial coefficient:", dp[n][r])
