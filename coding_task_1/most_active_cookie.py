import sys
import cookieFileParser

"""
Creates command that takes in specificed arguments of a csv file and -d date.

"""
def main():
    filename = sys.argv[1]
    d_identifier = sys.argv[2]
    if d_identifier != "-d":    # must be -d for date argument
        raise ValueError
    date = sys.argv[3]
    parseCookie = cookieFileParser.CookieFileParser(filename, date)
    parseCookie.readCookieFile()
    cookies_list = parseCookie.getMostActiveCookie()
    for cookie in cookies_list:
        sys.stdout.write(cookie + "\n")

if __name__ == "__main__":
    main()
