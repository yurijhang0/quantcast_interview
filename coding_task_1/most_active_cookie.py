import sys
import cookieFileParser
from datetime import datetime

"""
Creates command that takes in specificed arguments of a csv file and -d date.

"""
def main(argv):
    filename = argv[0]
    date_option = argv[1]
    date_value = argv[2]
    # argument testing to raise exceptions
    valid_date = not bool(datetime.strptime(date_value, "%Y-%m-%d")) or len(date_value.split("-")[1]) != 2 or len(date_value.split("-")[2]) != 2
    if len(argv) > 3 or date_option != "-d" or valid_date:
        raise ValueError
    # using cookieFileParser to get result and return result
    parseCookie = cookieFileParser.CookieFileParser(filename, date_value)
    parseCookie.readCookieFile()
    cookies_list = parseCookie.getMostActiveCookie()
    for cookie in cookies_list:
        sys.stdout.write(cookie + "\n")
    return cookies_list

if __name__ == "__main__":
    main(sys.argv[1:])
