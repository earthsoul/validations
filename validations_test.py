import validation
import unittest

class TestStringMethods(unittest.TestCase):
    @unittest.expectedFailure
    def test_allnumber(self):
        input = '123456'
        output = False
        self.assertEqual(input.validate_user(), output)

    @unittest.expectedFailure
    def test_empty(self):
        input = ''
        output = False
        self.assertEqual(input.validate_user(), output)

    def test_case1(self):
        input = 'earthsoul'
        output = True
        self.assertEqual(input.validate_user(),output)

if __name__ == '__main__':
    unittest.main()
