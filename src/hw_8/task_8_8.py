"""
Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
т. е. таким, которое читается одинаково слева направо и справа налево.
(Определить функцию, позволяющую распознавать слова палиндромы.)
"""


def is_palindrome(*args) -> None:
    """Function determines whether a word from the list is a palindrome"""
    for string in args:

        print(f"{string} is palindrome" if string == string[::-1] else f"{string} is not palindrome")


A = ['savvas', 'wertrew', 'sdgk', 'sjdkt']
is_palindrome(*A)

