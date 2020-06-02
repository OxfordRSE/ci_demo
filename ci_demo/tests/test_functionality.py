import unittest

import ci_demo


class TestFunctionality(unittest.TestCase):

    def test_greeting(self):
        greeting = ci_demo.greet()
        self.assertEqual(greeting, "Hello")


if __name__ == '__main__':
    unittest.main()
