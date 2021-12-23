import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import pandas
from selenium import webdriver

chromedriver_path = "c:/se/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path)

url = 'https://www.makaan.com/pune-property/hinjewadi-flats-for-sale-50221'

project_names = []
specifications = []
sizes = []
values = []
def houseScraping(website,page_number):
    next_page = website+"?"+"page="+str(page_number)
    driver.get(str(next_page))
    time.sleep(5)  # if you want to wait 3 seconds for the page to load
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='html.parser')

    for element in soup.findAll('li', attrs={'class': 'cardholder'}):
        value = element.find("div", attrs={"data-type": "price-link"})
        size = element.find("td", attrs={"class": "size"})
        specification = element.find("a", attrs={'class': 'typelink'})
        project_name = element.find("a", attrs={'class': 'projName'})
        if value and value.text:
            values.append(value.text)
        else:
            values.append('No data')
        if size and size.text:
            sizes.append(size.text)
        else:
            sizes.append('No data')

        if specification and specification.text:
            specifications.append(specification.text)

        else:
            specifications.append('No data')

        if project_name and project_name.text:
            project_names.append(project_name.text)

        else:
            project_names.append('No data')

    if page_number < 30:
        page_number += 1
        houseScraping(website,page_number)


houseScraping(url,1)



# project_name = soup.find("a", attrs = {'class':'projName'})
# print(project_name.text)
housing_data = pd.DataFrame({'Property Value':values,'Project':project_names,'Specifications':specifications,'Property Size':sizes })
housing_data.to_csv('D:/Projects/Gramworx/housing.csv')