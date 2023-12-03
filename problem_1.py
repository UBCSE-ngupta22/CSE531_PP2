def LCS(n, m):
    seq1 = len(n)
    seq2 = len(m)
    dp = [[0]*(seq2+1) for _ in range(seq1+1)]

    for i in range(seq1):
        for j in range(seq2):
            if n[i] == m[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    return dp, dp[seq1][seq2]


def sequencesLength(dp, lcs):
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j] == lcs:
                return i+j


# Input
n, m = input(), input()

dp, lcs = LCS(n, m)
totalLength = sequencesLength(dp, lcs)

# Output
for i in [lcs, totalLength]:
    print(i)
