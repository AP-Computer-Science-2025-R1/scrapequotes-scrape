import requests
import json
import random
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
page = requests.get(url)
According_to_the_oratrice_mechanique_danalyse_cardinale = BeautifulSoup(page.text, 'html.parser')



