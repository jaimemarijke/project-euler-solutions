# https://projecteuler.net/problem=5
# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# [1, 3, 4, 5] 60


# [1, 3*1, 2, 5*1] = 30

import collections
from functools import reduce
from operator import mul

from .problem3 import prime_factors


def _is_multiple(number, factors):
    return all(
        number % factor == 0
        for factor in factors
    )


def smallest_multiple(factors):
    ''' Returns the smallest number that is a multiple of all of the factors'''
    shared_prime_factors = collections.Counter()

    for factor in factors:
        # Represent the factor's prime factors as a Counter, e.g. for 60:
        # prime_factors(60) = [2, 2, 3, 5]
        # Counter(prime_factors(60)) = {
        #     2: 2,
        #     3: 1,
        #     5: 1,
        # }
        new_prime_factors = collections.Counter(prime_factors(factor))

        # For each factor in the list, add on any unique prime factors not already covered by smaller numbers
        shared_prime_factors += new_prime_factors - shared_prime_factors

    return reduce(mul, [factor ** count for factor, count in shared_prime_factors.items()])
