import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)
proxy = {'http': 'http://198.27.74.6:9300'}
url="https://internship.aicte-india.org/"
headers = {"User-Agent":  "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",}
response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.text)
headings=[]
companies=[]
duration=[]
cities=[]
start_date=[]
stipends=[]
apply_by=[]
type_time=[]
links=[]
link_start="https://internship.aicte-india.org/"
str=""
for i in soup.find_all("div",class_="container"):
    for link in i.find_all("div",class_="col-md-3"):
        #print(link)
        for a_tag in link.find_all("a"):
            href = a_tag.get('href')
            str=link_start+href
            links.append(str)
print(links)
  #  print(i.text)
    # for heading in i.find_all("div",class_="internship-primary-info"):
    #     for k in heading.find_all("div"):
    #         for j in heading.find_all("h3",class_="job-title"):
    #
    #             print(heading.text)
    #             headings.append(heading)
    # for company in i.find_all("h5",class_="company-name"):
    #     companies.append(company)
    # for city in i.find_all("li",class_="location"):
    #     cities.append(city)
    # for stipend in i.find_all("li",class_="stipend"):
    #     stipends.append(stipend)
    # for time in i.find_all("li",class_="duration"):
    #     duration.append(time)
    # for datetoapply in i.find_all("li",class_="apply-by"):
    #     apply_by.append(datetoapply)
#print(headings)
# print(companies)
# print(stipends)
# print(apply_by)
# print(duration)
# print(cities)
