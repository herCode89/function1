from task import conv_num
import unittest


class TestCase(unittest.TestCase):

    # Empty String and negative
    def test1_fun1(self):
        val = ''
        self.assertIsNone(conv_num(val))

    def test2_fun1(self):
        val = '-'
        self.assertIsNone(conv_num(val))

    # Test for -0x and 0x
    def test3_fun1(self):
        val = '-0x'
        self.assertIsNone(conv_num(val))

    def test4_fun1(self):
        val = '0x'
        self.assertIsNone(conv_num(val))

    # Test String of an Integer + and -
    def test5_fun1(self):
        val = '64731'
        self.assertEqual(conv_num(val), 64731)

    def test6_fun1(self):
        val = '-64731'
        self.assertEqual(conv_num(val), -64731)

    # Test Float with with decimal in fraction, after or with leading 0 and at multiple points
    def test7_fun1(self):
        val = '647.31'
        self.assertEqual(conv_num(val), 647.31)

    def test8_fun1(self):
        val = '647.'
        self.assertEqual(conv_num(val), 647.0)

    def test9_fun1(self):
        val = '0647'
        self.assertEqual(conv_num(val), 647)

    def test10_fun1(self):
        val = '.31'
        self.assertAlmostEqual(conv_num(val), 0.31)

    def test11_fun1(self):
        val = '64.7.31'
        self.assertIsNone(conv_num(val))

    # Test Hexadecimal in multiple settings
    def test12_fun1(self):
        val = '0xCF5'
        self.assertEqual(conv_num(val), 3317)

    def test13_fun1(self):
        val = '-0xAB'
        self.assertEqual(conv_num(val), -171)

    def test14_fun1(self):
        val = '0xFH5'
        self.assertIsNone(conv_num(val))

    def test15_fun1(self):
        val = '0xF.5'
        self.assertEqual(conv_num(val), 15.3125)

    def test16_fun1(self):
        val = '0xfH5'
        self.assertIsNone(conv_num(val))

    def test17_fun1(self):
        val = '64731F'
        self.assertIsNone(conv_num(val))

    def test18_fun1(self):
        val = '0xcf5'
        self.assertEqual(conv_num(val), 3317)

    def test19_fun1(self):
        val = '0x-CF5'
        self.assertIsNone(conv_num(val))


if __name__ == '__main__':
    unittest.main()
