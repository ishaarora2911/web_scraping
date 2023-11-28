from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
options=Options()
options.add_argument('--headless')
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
options.add_argument(f'user-agent={user_agent}')
service=Service('D:/path/to/chromedriver.exe')
proxy_address='http://123.456.789.10:8080'
options.add_argument(f'--proxy-server={proxy_address}')
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://internshala.com/internships/engineering-internship")
html_content=driver.page_source
soup=BeautifulSoup(html_content,'html.parser')
print(soup.text)