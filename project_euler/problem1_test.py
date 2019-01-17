import pytest

from . import problem1 as module


@pytest.mark.parametrize("multiple, x, expected", [
    (3, 6, True),
    (3, 7, False),
    (2, 4, True),
    (2, 5, False)
])
def test__is_multiple_of(multiple, x, expected):
    assert module._is_multiple_of(multiple, x) == expected


@pytest.mark.parametrize("below, expected", [
    (10, 23),
    (100, 2318),
    (1000, 233168),
])
def test_sum_of_multiples_of_3_and_5_below_value(below, expected):
    assert module.sum_of_multiples_of_3_and_5_below_value(below) == expected
