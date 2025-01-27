#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given total.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total.

    Args:
        coins (list): List of the values of coins in possession.
        total (int): Total amount to achieve.

    Returns:
        int: Fewest number of coins needed to achieve total or -1 if not possible.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    
    for coin in coins:
        if total <= 0:
            break
        num = total // coin
        count += num
        total -= num * coin

    return count if total == 0 else -1
