#!/usr/bin/python3
"""The Change Making Problem
    - Fewest Coins to make change
"""


def makeChange(coins, total):
    """Make Change Function
        - Get The coins, Total
        - Return fewest number
    """
    if(total <= 0):
        return -1
    n = len(coins)
    ans = []

    i = n - 1
    while(i >= 0):
        while(total >= coins[i]):
            total -= coins[i]
            ans.append(coins[i])
        i -= 1
    if i == -1 and total != 0:
        return -1
    return len(ans)
