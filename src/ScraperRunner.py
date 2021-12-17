from Scrapers.scraper_focsp import ScraperFOCSP
from Scrapers.scraper_abc import Scraper

def run():

    toRun = [
        ScraperFOCSP()
    ]

    for i in toRun:
        i.runScraper()
        
run()