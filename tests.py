import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        input = '1'
        expected = False
        self.assertEqual(check_pwd(input), expected)
    def test2(self):
        input = 'asgdjdsjfjsh'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        input = 'ASADAFSDGSDASF'
        expected = False
        self.assertEqual(check_pwd(input), expected)
    def test4(self):
        input = 'ASADAFSdsfsdf'
        expected = False
        self.assertEqual(check_pwd(input), expected)
    def test5(self):
        input = 'ASADAFSdsfsdf2'
        expected = False
        self.assertEqual(check_pwd(input), expected)
    def test5(self):
        input = 'ASAD@#Sdsfsdf2'
        expected = True
        self.assertEqual(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()