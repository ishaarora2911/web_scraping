from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

# Set up Chrome options
options = Options()
options.add_argument('--headless')  # Run in headless mode without opening a browser window

# Set up user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
options.add_argument(f'user-agent={user_agent}')
service = Service('D:\Downloads\chromedriver_win32.zip')
# Set up proxy
proxy_address = 'http://123.456.789.10:8080'
options.add_argument(f'--proxy-server={proxy_address}')

# Set the path to the Chrome driver executable
#chromedriver_path = 'D:\chromedriver.exe'   # Replace with the actual path to chrom6vedriver executable
driver = webdriver.Chrome(service=service, options=options)
# Set up Chrome driver with options and the driver executable path
#driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Load the webpage using Selenium
driver.get("https://internshala.com/internships/engineering-internship/")

# Wait for the dynamic content to load (you may need to adjust the wait time)
driver.implicitly_wait(10)

# Retrieve the HTML content from the loaded page
html_content = driver.page_source

# Create a BeautifulSoup object for parsing
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.text)

# Perform the data extraction using Beautiful Soup
Cities = []
for i in soup.find_all("div", class_="container-fluid individual_internship visibilityTrackerItem"):
    for location in i.find_all("div", id="location_names"):
        for sp in location.find_all("span"):
            for a_tag in i.find_all("a", class_="location_link view_detail_button"):
                data = a_tag.text.replace("\n", "").strip()
                Cities.append(data)

# Print the extracted city data
print(Cities)

# Close the Selenium WebDriver
driver.quit()
