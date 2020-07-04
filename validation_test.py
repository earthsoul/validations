from validations import vailidate_user
import unittest

class TestStringMethods(unittest.TestCase):
    @unittest.expectedFailure
    def test_allnumber(self):
        inputs = '123456'
        output = False
        self.assertEqual(vailidate_user(inputs,len(inputs)), output)

    @unittest.expectedFailure
    def test_empty(self):
        inputs = ''
        output = False
        self.assertEqual(vailidate_user(inputs,len(inputs)), output)

    def test_case1(self):
        inputs = 'earthsoul'
        output = True
        self.assertEqual(vailidate_user(inputs,len(inputs)),output)

if __name__ == '__main__':
    unittest.main()
