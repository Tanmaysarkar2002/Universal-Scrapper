# from pygooglenews.pygooglenews import GoogleNews

# gn = GoogleNews()
# s = gn.search('boeing OR airbus')

# for entry in s["entries"]:
#     print(entry["title"])


# from autoscraper import AutoScraper

# url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

# # We can add one or multiple candidates here.
# # You can also put urls here to retrieve urls.
# wanted_list = ["What are metaclasses in Python?"]

# scraper = AutoScraper()
# result = scraper.build(url, wanted_list)
# print(result)

# # from googlesearch.googlesearch import search
# from googlesearch.googlesearch import search
# for url in search('python software foundation'):
#     print(url)
# # Returns a list of SearchResult
# # Properties:
# # - title
# # - url
# # - description
# # search('"Breaking Code" WordPress blog')

from magic_google.magic_google import MagicGoogle
import pprint

# Or PROXIES = None
# PROXIES = [{
#     'http': 'http://192.168.2.207:1080',
#     'https': 'http://192.168.2.207:1080'
# }]

PROXIES = []

# Or MagicGoogle()
mg = MagicGoogle(PROXIES)

#  Crawling the whole page
# result = mg.search_page(query='python')
# print(result)

# # Crawling url
for url in mg.search_url(query='python'):
    if url != None and  'maps'  not in url:
        print(url)
# for url in mg.search(query='python', num=4):
#     # print(url['title'])
#     if url['title'] != '':
#             pprint.pprint(url)