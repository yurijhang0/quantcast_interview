import csv


"""
Class used to process the log file and return the most active cookie for specified day.

"""
class CookieFileParser:

    """
    Initializer for the parser.

    """
    def __init__(self, filename, date, trackerDict = {}):
        self.filename = filename
        self.date = date
        self.trackerDict = trackerDict

    """
    Opens log file and populates trackerDict with {cookie: counter} for only
    the specified date.

    """
    def readCookieFile(self):
        self.trackerDict = {}
        with open(self.filename, "r") as cookieFileIn:
            # loop through cookie csv line by line as string
            for cookieEntry in cookieFileIn:
                cookie = cookieEntry.split(",")[0]
                timeStamp = cookieEntry.split(",")[1]
                # track num of encounters w cookie using tracker dictionary
                if self.date in timeStamp:
                    if cookie in self.trackerDict:
                        self.trackerDict[cookie] += 1
                    else:
                        self.trackerDict[cookie] = 1

    """
    Using trackerDict, finds most active cookie for the specified date and
    returns the cookie.

    """
    def getMostActiveCookie(self):
        # return cookie key with max counter
        return max(self.trackerDict, key = self.trackerDict.get)
            
