def lcs(a: str, b: str):
    """
    Returns both the LCS length and the actual LCS string.
    """
    n = len(a)
    m = len(b)

    # DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find actual LCS string
    i, j = n, m
    lcs_str = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_str.append(a[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    lcs_str.reverse()
    return dp[n][m], "".join(lcs_str)


if __name__ == "__main__":
    print("🔵 Longest Common Subsequence Calculator\n")

    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")

    length, sequence = lcs(s1, s2)

    print("\n✅ LCS Length:", length)
    print("🧵 LCS Sequence:", sequence)
