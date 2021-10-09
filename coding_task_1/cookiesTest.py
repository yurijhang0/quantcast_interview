import unittest
import cookieFileParser

"""
Unit testing class for max active cookie finder.

"""
class CookiesTest(unittest.TestCase):
    
    # 0 expected cookie test
    def testZeroCookie(self):
        parseCookie = cookieFileParser.CookieFileParser("cookie_log1.csv", "2018-12-10")
        parseCookie.readCookieFile()
        result_list = parseCookie.getMostActiveCookie()
        expected_list = []
        self.assertEqual(expected_list, result_list, "List should contain no cookies.")

    # 1 expected cookie test
    def testOneCookie(self):
        parseCookie = cookieFileParser.CookieFileParser("cookie_log1.csv", "2018-12-09")
        parseCookie.readCookieFile()
        result_list = parseCookie.getMostActiveCookie()
        expected_list = ["AtY0laUfhglK3lC7"]
        self.assertEqual(expected_list, result_list, "List should only contain AtY0laUfhglK3lC7.")
    
    # 2 expected cookie test
    def testTwoCookie(self):
        parseCookie = cookieFileParser.CookieFileParser("cookie_log2.csv", "2018-12-09")
        parseCookie.readCookieFile()
        result_list = parseCookie.getMostActiveCookie()
        expected_list = ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA"]
        self.assertEqual(expected_list, result_list, "List should contain AtY0laUfhglK3lC7 and SAZuXPGUrfbcn5UA.")

    # invalid csv file test
    def testFileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            parseCookie = cookieFileParser.CookieFileParser("blah.csv", "2018-12-09")
            parseCookie.readCookieFile()
    
    

if __name__ == "__main__":
    unittest.main()