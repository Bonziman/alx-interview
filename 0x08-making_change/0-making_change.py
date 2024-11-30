#!/usr/bin/python3
"""
    model with a function to calculate minimum number of coins needed
    to make the a pregiven total
"""
def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given amount `total`.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The total amount of money you want to make change for.

    Returns:
        int: The minimum number of coins needed to make the change for the given total.
             If the total cannot be met by any combination of the coins, return -1.
    """
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

    # If dp[total] is still 'inf',
    # it means the total cannot be met by any combination of coins
    return dp[total] if dp[total] != float('inf') else -1
