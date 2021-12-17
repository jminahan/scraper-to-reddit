from abc import ABC, abstractmethod

class Scraper(ABC):
   @abstractmethod
   def runScraper(self):
      pass

   @abstractmethod
   def parseWebpage(self, webPageContent):
      pass