from Scrapers.scraper_abc import Scraper
from ScraperUtils.RequestWrapper import *
from bs4 import BeautifulSoup
from GeneralUtils.genutils import *
class ScraperFOCSP(Scraper):
    def __init__(self):
        pass

    def runScraper(self):
      print(
          self.parseWebpage(
        getWebPageHTML("https://congresssquarepark.org/events/")["content"]))

    def parseWebpage(self, webPageContent):
        soup = BeautifulSoup(webPageContent, 'html.parser')
        daysOfInterest = dayNums(rangeOfNextDays=7)
        calendar = soup.find(class_="tribe-events-calendar")
        calendarDaysOfInterest = []
        for i in daysOfInterest:
            divIdOfInterest = "tribe-events-daynum-" + str(i) + "-0"
            calendarItem = calendar.find(id=divIdOfInterest).find_next_sibling("div")
            if(calendarItem != None):
                calendarDaysOfInterest.append(calendarItem.findChild("h3"))

        return calendarDaysOfInterest