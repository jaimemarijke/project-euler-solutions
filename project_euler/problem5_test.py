import pytest

from . import problem5 as module


@pytest.mark.parametrize("factors, expected", [
    (range(1, 3), 2),
    (range(1, 11), 2520),
    (range(2, 11), 2520),
    (list(range(1, 11)) + [16], 5040),
    (range(1, 19), 12252240),
    (range(1, 21), 232792560),
])
def test_smallest_multiple(factors, expected):
    assert module.smallest_multiple(factors) == expected


@pytest.mark.parametrize("number, factors, expected", [
    (1, [1], True),
    (1, [2, 1], False),
    (10, [1, 2, 5, 10], True),
    (10, [1, 2, 3, 10], False),
    (2520, range(1, 11), True),
])
def test_is_multiple(number, factors, expected):
    assert module._is_multiple(number, factors) == expected
