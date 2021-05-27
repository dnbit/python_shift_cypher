import unittest
from cypher import *


class TestCypher(unittest.TestCase):

    def test_cypher_basic(self):
        input = "HELLO"
        actual = cypher(input)
        expected = "KHOOR"
        message = "Should be " + expected
        self.assertEqual(actual, expected, message)

    def test_cypher_ZA(self):
        input = "WXYZABC"
        actual = cypher(input)
        expected = "ZABCDEF"
        message = "Should be " + expected
        self.assertEqual(actual, expected, message)

    def test_cypher_input_empty(self):
        input = ""
        actual = cypher(input)
        expected = ""
        message = "Should be " + expected
        self.assertEqual(actual, expected, message)

    def test_cypher_input_invalid(self):
        input = "123"
        with self.assertRaises(ValueError):
            cypher(input)

    def test_cypher_input_none(self):
        input = None
        with self.assertRaises(TypeError):
            cypher(input)

    def test_decypher_basic(self):
        input = "KHOOR"
        actual = decypher(input)
        expected = "HELLO"
        message = "Should be " + expected
        self.assertEqual(actual, expected, message)

    def test_decypher_ZA(self):
        input = "ZABCDEF"
        actual = decypher(input)
        expected = "WXYZABC"
        message = "Should be " + expected
        self.assertEqual(actual, expected, message)

    def test_decypher_input_empty(self):
        input = ""
        actual = decypher(input)
        expected = ""
        message = "Should be " + expected
        self.assertEqual(actual, expected, message)

    def test_decypher_input_invalid(self):
        input = "123"
        with self.assertRaises(ValueError):
            decypher(input)

    def test_decypher_input_none(self):
        input = None
        with self.assertRaises(TypeError):
            cypher(input)


if __name__ == '__main__':
    unittest.main()
