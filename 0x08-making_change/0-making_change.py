#!/usr/bin/python3
def makeChange(coins, total):
    # If total is 0 or less, return 0 (no coins needed)
    if total <= 0:
        return 0

    # Initialize DP array with 'inf' for all amounts except 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make total 0

    # Iterate through each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still 'inf'
    return dp[total] if dp[total] != float('inf') else -1
