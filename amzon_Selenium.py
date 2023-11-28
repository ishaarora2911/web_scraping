from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Replace "path_to_chromedriver" with the actual path to the ChromeDriver executable
path_to_chromedriver = "D:/path/to/chromedriver.exe"

# Create a Service object with the path to the ChromeDriver executable
service = Service(path_to_chromedriver)

# Create ChromeOptions object
options = Options()

#Add proxy server
# proxy_server = 'https://198.27.74.6:9300'
# options.add_argument(f'--proxy-server={proxy_server}')

# Add user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
options.add_argument(f'user-agent={user_agent}')

# Initialize Chrome WebDriver, passing the Service and Options objects
browser = webdriver.Chrome(service=service, options=options)
timeout = 10
browser.set_page_load_timeout(timeout)
# Now you can interact with the browser using the 'browser' object
# For example:
browser.get("https://internshala.com/internships/engineering-internship")

# Get the page source after it has loaded
page_source = browser.page_source

# Pass the page source to BeautifulSoup for parsing
soup = BeautifulSoup(page_source, 'html.parser')
print(soup.text)
Cities = []
for i in soup.find_all("div", class_="container-fluid individual_internship visibilityTrackerItem"):
    for location in i.find_all("div", id="location_names"):
        for sp in location.find_all("span"):
            for a_tag in i.find_all("a", class_="location_link view_detail_button"):
                data = a_tag.text.replace("\n", "").strip()
                Cities.append(data)

# Print the extracted city data
print(Cities)

# Now you can use BeautifulSoup methods to parse the HTML and extract data
# For example, find all the <a> tags with the class "link" and print their text
# links = soup.find_all('a', class_='link')
# for link in links:
#     print(link.get_text())

# Close the browser session
browser.quit()
