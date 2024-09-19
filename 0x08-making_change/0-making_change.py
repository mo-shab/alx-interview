#!/usr/bin/python3
"""The Change Making Problem
    - Fewest Coins to make change
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to make change"""
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
