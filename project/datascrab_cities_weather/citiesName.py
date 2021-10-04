import requests
from bs4 import BeautifulSoup

URL = "https://mausam.imd.gov.in/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='today')
title = results.find('h2').text.strip()
print(title,'\n')
city_element = results.find_all('div',class_='capitals clearfix')
element_list = results.find_all('div',class_='capital')

print(len(element_list))
for job_element in element_list:
    city__element = job_element.find('h3').text.strip()
    temp__element = job_element.find('span',class_='val').text.strip()
    wind__element = job_element.find('p',class_='wind').text.strip()
    rainChance__element = job_element.find('span',class_='max').text.strip()
    st = 'city:  {}, temp:  {}, wind speed:  {}, rain chances:  {}'.format(city__element, temp__element, wind__element,rainChance__element)
    print(st)