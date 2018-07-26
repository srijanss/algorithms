"""
Algorithms
"""

class Solutions(object):
    """
    Algorithms
    """

    def __init__(self):
        pass

    def sieve_algorithm(self, limit):
        """
        Sieve's Algorithm to find primes
        """
        prime_arr = [True if i != 1 else False for i in range(1, limit + 1)] 
        p = 2
        while p * p <= limit:
            if prime_arr[p - 1] == True:
                for i in range(p*2, limit+1, p):
                    prime_arr[i - 1] = False 
            p += 1
        return prime_arr