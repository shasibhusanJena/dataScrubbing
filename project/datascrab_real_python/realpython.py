import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id='ResultsContainer')
# print(results.prettify())
job_elements = results.find_all('div', class_='card-content')
# for job_element in job_elements:
#     print(job_element, end='\n'*2)

for job_element in job_elements:
    title_element = job_element.find('h2',class_='title')
    company_element = job_element.find('h3',class_='company')
    location_element = job_element.find('p',class_='location')

    title_element = title_element.text.strip()
    company_element = company_element.text.strip()
    location_element = location_element.text.strip()
    st = 'title:  {}, company:  {}, location:  {}'.format(title_element,company_element,location_element)
    print(st)