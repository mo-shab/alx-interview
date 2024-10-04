#!/usr/bin/python3
"""Prime Number"""

def isWinner(x, nums):
    """Function for Prime Number, is winner"""
    # Function to generate prime numbers up to the maximum n
    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    # Find the maximum value in nums to create the sieve up to that value
    max_n = max(nums)
    primes = sieve(max_n)

    # Function to determine the winner for a single game with n
    def play_game(n):
        """Function to play game"""
        if n == 1:
            return "Ben"  # No prime numbers, Maria can't make a move

        moves = 0  # Count moves, Maria is first if moves is even, Ben if odd
        available = [True] * (n + 1)

        for p in range(2, n + 1):
            if primes[p] and available[p]:
                # Make the move for current player (prime p is chosen)
                moves += 1
                # Remove prime and its multiples
                for multiple in range(p, n + 1, p):
                    available[multiple] = False

        return "Maria" if moves % 2 == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    # Play x rounds of the game
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
