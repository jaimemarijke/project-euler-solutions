import pytest

from . import problem3 as module


#     1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
@pytest.mark.parametrize("x, expected", [
    (1, {1}),
    (2, {1, 2}),
    (3, {1, 3}),
    (4, {1, 2, 4}),
    (5, {1, 5}),
    (13195, {1, 5, 7, 13, 29, 35, 65, 91, 145, 203, 377, 455, 1015, 1885, 2639, 13195}),
])
def test_factors(x, expected):
    assert module.factors(x) == expected


@pytest.mark.parametrize("x, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (29, True),
    (13195, False),
])
def test_is_prime(x, expected):
    assert module._is_prime(x) == expected


@pytest.mark.parametrize("x, expected", [
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (5, [5]),
    (10, [2, 5]),
    (15, [3, 5]),
    (13195, [5, 7, 13, 29]),
])
def test_prime_factors(x, expected):
    assert module.prime_factors(x) == expected


@pytest.mark.parametrize("x, expected", [
    (1, None),
    (2, 2),
    (3, 3),
    (4, 2),
    (5, 5),
    (15, 5),
    (13195, 29),
    (600851475143, 6857)
])
def test_largest_prime_factor(x, expected):
    assert module.largest_prime_factor(x) == expected


@pytest.mark.parametrize("invalid_input", [
    (-1),
    (0),
    (1.5),
])
def test_larges_prime_factor_raises_on_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        module.largest_prime_factor(invalid_input)
