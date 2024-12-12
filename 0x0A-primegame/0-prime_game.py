#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    
    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.
    
    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben"), or None if it's a tie.
    """
    if not nums or x <= 0:
        return None

    # Helper function to generate a list of primes up to the maximum number in nums
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    # Find the maximum n in nums to optimize prime number computation
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Number of primes up to n determines the number of moves
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
