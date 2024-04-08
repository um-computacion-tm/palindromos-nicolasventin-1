import unittest

def is_palindrome(value):
    reversevalue = value[::-1]
    if value == reversevalue:
        return True
    else:
        return False

unittest.main()