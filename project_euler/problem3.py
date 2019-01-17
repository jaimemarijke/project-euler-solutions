# Largest Prime Factor
# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143


def _guard_is_positive_integer(number):
    if number <= 0 or type(number) != int:
        raise ValueError('Only positive integers allowed')


def factors(number):
    _guard_is_positive_integer(number)

    return set([
        possible_factor
        for possible_factor in range(1, number + 1)
        if number % possible_factor == 0
    ])


def _is_prime(number):
    return len(factors(number)) == 2


# def prime_factors(number):
#     return [
#         factor
#         for factor in factors(number)
#         if _is_prime(factor)
#     ]


def prime_factors(number):
    ''' Recursively find prime factors. Should be more efficient'''
    _guard_is_positive_integer(number)

    if number == 1:
        return []

    for possible_factor in range(2, int(number)+1):
        if number % possible_factor == 0:
            return [possible_factor] + prime_factors(int(number / possible_factor))


def largest_prime_factor(number):
    prime_factors_of_number = prime_factors(number)
    return max(prime_factors_of_number) if prime_factors_of_number else None
