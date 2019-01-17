# Multiples of 3 and 5
# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from functools import partial
import itertools


def _is_multiple_of(multiple, x):
    return x % multiple == 0


def _multiples_in_list(multiple, list_of_integers):
    return list(filter(partial(_is_multiple_of, multiple), list_of_integers))


def _flatten(list_of_lists):
    return list(itertools.chain(*list_of_lists))


def multiples_below_value(below, multiples):
    integers_below_value = list(range(0, below))

    return set(_flatten([
        _multiples_in_list(multiple, integers_below_value)
        for multiple in multiples
    ]))


def sum_of_multiples_of_3_and_5_below_value(below):
    multiples_of_3_and_5 = multiples_below_value(below, multiples=[3, 5])
    return sum(multiples_of_3_and_5)
