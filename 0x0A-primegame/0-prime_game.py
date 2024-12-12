#!/usr/bin/python3
"""
Module for solving the Prime Game problem.

This module implements a game where players take turns selecting prime numbers
and removing them along with their multiples from a set of consecutive integers.
"""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): Number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def play_prime_game(n):
    """
    Simulate a single round of the Prime Game.

    Args:
        n (int): Upper limit of the set of numbers.

    Returns:
        str: Name of the winner ('Maria' or 'Ben').
    """
    numbers = set(range(1, n + 1))
    current_player = 'Maria'

    while True:
        primes = [num for num in numbers if is_prime(num)]

        if not primes:
            return 'Ben' if current_player == 'Maria' else 'Maria'

        chosen_prime = min(primes)
        numbers = {num for num in numbers if num % chosen_prime != 0}
        current_player = 'Ben' if current_player == 'Maria' else 'Maria'


def isWinner(x, nums):
    """
    Determine the overall winner across multiple rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of maximum numbers for each round.

    Returns:
        str or None: Name of the player with most wins.
    """
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_prime_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
