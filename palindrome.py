"""
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.
678 is not a palindrome. Do not convert the integer into a string.
"""


def is_palindrome(number: int):
    if number < 10:
        return True
    digits = []
    tmp_number = number
    while tmp_number >= 1:
        digits.append(tmp_number % 10)
        tmp_number = tmp_number // 10
    return digits == digits[::-1]


def test_solution():
    assert is_palindrome(0)
    assert is_palindrome(1)
    assert not is_palindrome(10)
    assert is_palindrome(888)
    assert not is_palindrome(123)
    assert not is_palindrome(123131444)
    assert is_palindrome(121)
