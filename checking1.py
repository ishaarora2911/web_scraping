import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
import random
import pandas as pd

# Rest of the code...
url = "https://internship.aicte-india.org/"
proxies = [
    'http://68.132.12.228:8888',
    'http://200.105.215.22:33630',
    'http://14.32.161.114:8080'
    # Add more proxies as needed
]

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    # Add more user agents as needed
]

# Randomly select a proxy and user agent
random_proxy = random.choice(proxies)
random_user_agent = random.choice(user_agents)
# Set up Chrome WebDriver with the selected proxy and user agent
options = webdriver.ChromeOptions()
options.add_argument(f'--proxy-server={random_proxy}')
options.add_argument(f'user-agent={random_user_agent}')

# Set the path to your ChromeDriver executable
webdriver_path = 'D:\Downloads\chromedriver_win32'
# Replace with the path to the newly downloaded ChromeDriver executable

# Initialize the WebDriver with error handling
try:
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    # Wait between 1 and 5 seconds before each request
    time_delay = random.uniform(1, 5)

    # Scrape the website
    driver.get(url)
    time.sleep(time_delay)
    page_source = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the data you need using BeautifulSoup
    links = []
    link_start = "https://internship.aicte-india.org/"
    str=""
    for i in soup.find_all("div", class_="container"):
        for link in i.find_all("div", class_="col-md-3"):
            for a_tag in link.find_all("a"):
                href = a_tag.get('href')
                str = link_start + href
                links.append(str)

    # Print the scraped links
    print("links=",links)

    # Iterate over each link and extract the desired information
    headings = []
    companies = []
    cities = []
    stipends = []
    durations = []
    apply_bys = []

    for link in links:
        try:
            driver.get(link)
            time.sleep(time_delay)
            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'html.parser')
            print(soup.text)
            for card in soup.find_all("div", class_="card-body"):
                for i in soup.find_all("div", class_="internship-info"):
                    for heading in i.find_all("div", class_="internship-primary-info"):
                        for k in heading.find_all("div"):
                            for j in k.find_all("h3", class_="job-title"):
                                headings.append(j.text)
                    for company in i.find_all("h5", class_="company-name"):
                        companies.append(company.text)
                    for city in i.find_all("li", class_="location"):
                        cities.append(city.text)
                    for stipend in i.find_all("li", class_="stipend"):
                        stipends.append(stipend.text)
                    for time in i.find_all("li", class_="duration"):
                        durations.append(time.text)
                    for datetoapply in i.find_all("li", class_="apply-by"):
                        apply_bys.append(datetoapply.text)

        except Exception as e:
            print("Error scraping link:", link, e)

    # Print the scraped data
    print("Headings:", headings)
    print("Companies:", companies)
    print("Cities:", cities)
    print("Stipends:", stipends)
    print("Durations:", durations)
    print("Apply by:", apply_bys)

    # Write the data to an Excel file
    data = {
        'Headings': headings,
        'Companies': companies,
        'Cities': cities,
        'Stipends': stipends,
        'Durations': durations,
        'Apply By': apply_bys
    }

    df = pd.DataFrame(data)
    df.to_excel('internship_data.xlsx', index=False)
    print("Data written to Excel file 'internship_datas.xlsx'")

except WebDriverException as e:
    print("Error initializing WebDriver:", e)

finally:
    # Close the WebDriver
    if 'driver' in locals() or 'driver' in globals():
        driver.quit()
