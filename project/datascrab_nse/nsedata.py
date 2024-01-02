import requests
from bs4 import BeautifulSoup

URL = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

