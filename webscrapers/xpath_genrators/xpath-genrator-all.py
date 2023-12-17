# import xpath as xp
# import sys

# from xpath import dsl as x
# from xpath.renderer import to_xpath

# expression = x.descendant("ul")[x.attr("id") == "foo"]
# xpath = to_xpath(expression)
# print(xpath)

# from xpath.html import button
from xpath.renderer import to_xpath

# print(to_xpath(button("Save"), exact=True))

from xpath.html import table

import requests

r = requests.get("https://www.sec.gov/litigation/fairfundlist-archive#ameriprise")

table = to_xpath(table('table'), exact=True)
print(table)