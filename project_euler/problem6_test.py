import pytest

from . import problem6 as module


# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 14),
    (range(1, 11), 385),
])
def test_sum_of_squares(numbers, expected):
    assert module.sum_of_squares(numbers) == expected


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 36),
    (range(1, 11), 3025),
])
def test_square_of_sum(numbers, expected):
    assert module.square_of_sum(numbers) == expected


@pytest.mark.parametrize("up_to_n, expected", [
    (3, 22),
    (10, 2640),
    (100, 25164150),
])
def test_difference(up_to_n, expected):
    assert module.difference(up_to_n) == expected
