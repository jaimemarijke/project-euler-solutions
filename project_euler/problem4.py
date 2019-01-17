# https://projecteuler.net/problem=4
# Largest palindrome product

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def _guard_is_positive_integer(number):
    if number <= 0 or type(number) != int:
        raise ValueError('Only positive integers allowed')


def _is_palindrome(number):
    backwards_number = int(''.join(reversed(str(number))))
    return number == backwards_number


def _numbers_with_n_digits(n_digits):
    _guard_is_positive_integer(n_digits)
    return range(10 ** (n_digits - 1), 10 ** n_digits)


def largest_palindrome_product(n_digits):
    numbers_with_n_digits = _numbers_with_n_digits(n_digits)
    products = (
        number_a * number_b
        for number_a in numbers_with_n_digits
        for number_b in numbers_with_n_digits
    )

    palindromes = filter(
        _is_palindrome,
        products
    )

    return max(palindromes)
