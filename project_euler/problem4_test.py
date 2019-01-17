import pytest

from . import problem4 as module


@pytest.mark.parametrize("number, expected", [
    (1, True),
    (2, True),
    (10, False),
    (11, True),
    (110, False),
    (808, True),
    (9009, True),
])
def test_is_palindrome(number, expected):
    assert module._is_palindrome(number) == expected


@pytest.mark.parametrize("n_digits, expected", [
    (1, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (2, range(10, 100)),
    (3, range(100, 1000)),
])
def test_numbers_with_n_digits(n_digits, expected):
    assert list(module._numbers_with_n_digits(n_digits)) == list(expected)


def test_numbers_with_n_digits_spot_check():
    actual = module._numbers_with_n_digits(3)
    assert {100, 101, 999}.issubset(actual)
    assert {99, 1000}.isdisjoint(actual)


@pytest.mark.parametrize("n_digits, expected", [
    (1, 9),
    (2, 9009),
    (3, 906609),
])
def test_largest_palindrome(n_digits, expected):
    assert module.largest_palindrome_product(n_digits) == expected
