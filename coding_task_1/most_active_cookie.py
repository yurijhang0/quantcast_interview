import sys
import cookieFileParser

"""
Creates command that takes in specificed arguments of a csv file and -d date.

"""
def main():
    try:    # must have all specified arguments
        filename = sys.argv[1]
        d_identifier = sys.argv[2]
        if d_identifier != "-d":    # must be -d for date argument
            raise Exception
        date = sys.argv[3]
        parseCookie = cookieFileParser.CookieFileParser(filename, date)
        parseCookie.readCookieFile()
        cookies_list = parseCookie.getMostActiveCookie()
        for cookie in cookies_list:
            sys.stdout.write(cookie + "\n")
    except: # raises exception if command does not contain all specified arguments
        raise SystemExit(f"Make sure to run the command like so:\npython most_active_cookie.py <cookie_log.csv> -d <date (year-month-day)>")

if __name__ == "__main__":
    main()
