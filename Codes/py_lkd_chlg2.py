"""
Title: Valuating Palindromes

Details: Python challenge to make a string reader that says if the input is a palindrome or not.

Input: String to evaluate
Output: Boolean value
Constrains:
    - Only consider letters (a-z)
    - Ignore casa ('A'=='a')
"""


def checkPalindrome(word):
    return ((word == word [::-1]) and word.isalpha())

checkPalindrome("Kaiak")