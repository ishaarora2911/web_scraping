import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

# Set up Chrome WebDriver
webdriver_path = 'D:\Downloads\chromedriver_win32'
options = webdriver.ChromeOptions()

# Add a random proxy



# Add a random user agent
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    # Add more user agents as needed
]
random_user_agent = random.choice(user_agents)
options.add_argument(f'user-agent={random_user_agent}')

driver = webdriver.Chrome(service=Service(webdriver_path), options=options)

# Define the URL
url = "https://in.linkedin.com/jobs/internship-jobs?position=1&pageNum=0"

try:
    # Wait for a random time delay between 1 and 5 seconds
    time_delay = random.uniform(1, 5)
    time.sleep(time_delay)

    # Get the page source and create a BeautifulSoup object
    driver.get(url)
    time.sleep(5)  # Adjust the sleep time as needed

    # Get the page source and create a BeautifulSoup object
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract the desired information using BeautifulSoup
    Position = []
    Companies = []
    Cities = []
    Stipend = []
    Apply_by = []
    Hiring_actively=[]
    for city in soup.find_all("span", class_="job-search-card__location"):
        if city.text == "":
            city.text = "-"
        Cities.append(city.text)
    for hiring_status in soup.find_all("span", class_="result-benefits__text"):
        if hiring_status.text == "":
            hiring_status.text = "-"
        Hiring_actively.append(hiring_status.text)
    for pos in soup.find_all("h3", class_="base-search-card__subtitle"):
        if pos.text == "":
            pos.text = "-"
        Position.append(pos.text)

    for company in soup.find_all("a", class_="hidden-nested-link"):
        if company.text == "":
            company.text = "-"
        Companies.append(company.text)



    # Close the WebDriver
    driver.quit()
    max_length = max(len(Position), len(Companies), len(Cities), len(Stipend), len(Apply_by))

    # Pad arrays with empty values to match the maximum length
    Position += [''] * (max_length - len(Position))
    Companies += [''] * (max_length - len(Companies))
    Cities += [''] * (max_length - len(Cities))
    Stipend += [''] * (max_length - len(Stipend))
    Apply_by += [''] * (max_length - len(Apply_by))

    # Write the data to an Excel file
    data = {
        'Position': Position,
        'Companies': Companies,
        'Cities': Cities,
        'Stipend': Stipend,
        'Apply By': Apply_by
    }

    df = pd.DataFrame(data)
    df.to_excel('internship_data.xlsx', index=False)
    print("Data written to Excel file 'internship_data.xlsx'")

except Exception as e:
    print("Error:", e)
