import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

time.sleep(1)
proxy = {'http': 'http://45.61.187.67:4007'}
url = "https://internshala.com/internships/engineering-internship/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

Type = []
Hiring_actively = []
Position = []
Companies = []
Cities = []
Stipend = []
Apply_by = []
Duration = []

for card in soup.find_all("div", class_="internship_meta"):
    actively_hiring_tags = card.find_all("div", class_="actively_hiring_badge")
    if actively_hiring_tags:
        for actively_hiring in actively_hiring_tags:
            span_tags = actively_hiring.find_all("span")
        if span_tags:
            for i in span_tags:
                try:
                    data = i.text.replace("\n", "").strip()
                    Hiring_actively.append(data)
                except AttributeError:
                    Hiring_actively.append("N/A")
        else:
            Hiring_actively.append("N/A")
    else:
        Hiring_actively.append("N/A")

    for header in card.find_all("div", class_="individual_internship_header"):
        for head in header.find_all("div", class_="company"):
            for pos in head.find_all("h3", class_="heading_4_5 profile"):
                for a in pos.find_all("a", class_="view_detail_button"):
                    try:
                        data = a.text.strip()
                        Position.append(data)
                    except AttributeError:
                        Position.append("N/A")
            for company in head.find_all("h4", class_="heading_6 company_name"):
                data = company.text.replace("\n", "").strip()
                Companies.append(data)

for i in soup.find_all("div", class_="container-fluid individual_internship visibilityTrackerItem"):
    for location in i.find_all("div", id="location_names"):
        for sp in location.find_all("span"):
            for a_tag in sp.find_all("a", class_="location_link view_detail_button"):
                data = a_tag.text.replace("\n", "").strip()
                Cities.append(data)

for other_details in soup.find_all("div", class_="internship_other_details_container"):
    stipend_tags = other_details.find_all("div", class_="other_detail_item_row")
    if stipend_tags:
        for i in other_details.find_all("div", class_="other_detail_item_row"):
            for j in i.find_all("div", class_="other_detail_item stipend_container"):
                for stipend in j.find_all('span', class_='stipend'):
                    data = stipend.text.replace("\n", "").strip()
                    Stipend.append(data)

# Check the lengths of arrays
# print(f'Hiring_actively length: {len(Hiring_actively)}')
# print(f'Position length: {len(Position)}')
# print(f'Companies length: {len(Companies)}')
# print(f'Cities length: {len(Cities)}')
# print(f'Stipend length: {len(Stipend)}')

# Equalize the lengths of arrays
length = max(len(Hiring_actively), len(Position), len(Companies), len(Cities), len(Stipend))

Hiring_actively += ['N/A'] * (length - len(Hiring_actively))
Position += ['N/A'] * (length - len(Position))
Companies += ['N/A'] * (length - len(Companies))
Cities += ['N/A'] * (length - len(Cities))
Stipend += ['N/A'] * (length - len(Stipend))

# Check the lengths of arrays after equalizing
# print(f'After equalizing:')
# print(f'Hiring_actively length: {len(Hiring_actively)}')
# print(f'Position length: {len(Position)}')
# print(f'Companies length: {len(Companies)}')
# print(f'Cities length: {len(Cities)}')
# print(f'Stipend length: {len(Stipend)}')

# Create DataFrame and save as Excel file
df = pd.DataFrame({
    'Hiring Actively': Hiring_actively,
    'Position': Position,
    'Company': Companies,
    'City': Cities,
    'Stipend': Stipend
})

df.to_excel('internship_dass.xlsx', index=False)

