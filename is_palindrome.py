import unittest


def is_palindrome(value):
    reversevalue = value[::-1]
    if value == reversevalue:
        return True
    else:
        return False


class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        value = "a"
        result = is_palindrome(value)
        self.assertTrue(result)

    def test_with_ala(self):
        value = "ala"
        result = is_palindrome(value)
        self.assertTrue(result)

    def test_with_neuquen(self):
        value = "neuquen"
        result = is_palindrome(value)
        self.assertTrue(result)

    def test_with_hola(self):
        value = "hola"
        result = is_palindrome(value)
        self.assertFalse(result)
    
    def test_with_panqueua(self):
        value = "panqueua"
        result = is_palindrome(value)
        self.assertFalse(result)

unittest.main()