import pytest

from . import problem2 as module


#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
@pytest.mark.parametrize("below, expected", [
    (1, 0),
    (2, 0),
    (3, 2),
    (5, 2),
    (8, 2),
    (9, 10),
    (13, 10),
    (21, 10),
    (34, 10),
    (35, 44),
    (100, 44),
])
def test_sum_of_even_fibonaccis(below, expected):
    assert module.sum_of_even_fibonaccis(below) == expected


# 0, 1, 1, 2, 3, 5, 8
@pytest.mark.parametrize("below, expected", [
    (1, [0]),
    (2, [0, 1, 1]),
    (3, [0, 1, 1, 2]),
    (4, [0, 1, 1, 2, 3]),
    (5, [0, 1, 1, 2, 3]),
])
def test_fibonacci_up_to(below, expected):
    assert module.fibonacci_up_to(below) == expected
