from .autoscraper import AutoScraper
from .pygooglenews.pygooglenews import GoogleNews
from bs4 import BeautifulSoup


import undetected_chromedriver as uc
from .magic_google.magic_google import MagicGoogle
import pprint




class unscrapper:

    def __init__(self) -> None:
        self.driver = "hi"
        

    def news_scrapper(self , keyword):
        gn = GoogleNews()
        s = gn.search(keyword)

        titles = []
        for entry in s["entries"]:
            titles.append(entry["title"])
        return titles
    
    def scrape_list(self , url , keyword):

        # We can add one or multiple candidates here.
        # You can also put urls here to retrieve urls.
        wanted_list = [keyword]
        print(wanted_list , url)

        scraper = AutoScraper()
        result = scraper.build(url, wanted_list)

        return result
    
    def scrape_url(self , keyword):
        url_list = []
        mg = MagicGoogle()
        for url in mg.search_url(query=keyword):
            if url != None and  'maps'  not in url:
                url_list.append(url)
        
        return url_list
    
    def scrape_page(self , keyword):
        url_list = []
        mg = MagicGoogle()
        for url in mg.search(query=keyword , num=10):
           
            if url['title'] != '':
        #       pprint.pprint(url)
                url_list.append(url)
        
        return url_list

