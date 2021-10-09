import unittest
import cookieFileParser
import most_active_cookie

"""
Unit testing class for max active cookie finder.

"""
class CookiesTest(unittest.TestCase):
    
    # 0 expected cookie test
    def testZeroCookie(self):
        result_list = most_active_cookie.main(["cookie_log1.csv", "-d", "2018-12-10"])
        expected_list = []
        self.assertEqual(expected_list, result_list, "List should contain no cookies.")

    # 1 expected cookie test
    def testOneCookie(self):
        result_list = most_active_cookie.main(["cookie_log1.csv", "-d", "2018-12-09"])
        expected_list = ["AtY0laUfhglK3lC7"]
        self.assertEqual(expected_list, result_list, "List should only contain AtY0laUfhglK3lC7.")
    
    # 2 expected cookie test
    def testTwoCookie(self):
        result_list = most_active_cookie.main(["cookie_log2.csv", "-d", "2018-12-09"])
        expected_list = ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA"]
        self.assertEqual(expected_list, result_list, "List should contain AtY0laUfhglK3lC7 and SAZuXPGUrfbcn5UA.")

    # invalid csv file test
    def testFileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            most_active_cookie.main(["blah.csv", "-d", "2018-12-09"])
    
    # too few args test
    def testFewArgs(self):
        with self.assertRaises(IndexError):
            most_active_cookie.main(["cookie_log1.csv", "-d"])
    
    # too many args test
    def testTooManyArgs(self):
        with self.assertRaises(ValueError):
            most_active_cookie.main(["cookie_log1.csv", "-d", "2018-12-09", "blah"])

    # invalid date option test (not -d in command line)
    def testInvalidDateOption(self):
        with self.assertRaises(ValueError):
            most_active_cookie.main(["cookie_log1.csv", "-t", "2018-12-09"])

    # invalid date value test 1 ... incorrect day formatting
    def testInvalidDateValue1(self):
        with self.assertRaises(ValueError):
            most_active_cookie.main(["cookie_log1.csv", "-d", "2018-12-9"])

    # invalid date value test 2 ... invalid day value
    def testInvalidDateValue2(self):
        with self.assertRaises(ValueError):
            most_active_cookie.main(["cookie_log1.csv", "-d", "2018-12-40"])

    # invalid date value test 3 ... incorrect month formatting
    def testInvalidDateValue3(self):
        with self.assertRaises(ValueError):
            most_active_cookie.main(["cookie_log1.csv", "-d", "2018-1-09"])

    # invalid date value test 4 ... incorrect month value
    def testInvalidDateValue4(self):
        with self.assertRaises(ValueError):
            most_active_cookie.main(["cookie_log1.csv", "-d", "2018-40-09"])
    
    # invalid date value test 5 ... incorrect year formatting
    def testInvalidDateValue5(self):
        with self.assertRaises(ValueError):
            most_active_cookie.main(["cookie_log1.csv", "-d", "1_32-12-09"])

    # invalid date value test 6 ... incorrect year value
    def testInvalidDateValue6(self):
        with self.assertRaises(ValueError):
            most_active_cookie.main(["cookie_log1.csv", "-d", "209-12-09"])

if __name__ == "__main__":
    unittest.main()