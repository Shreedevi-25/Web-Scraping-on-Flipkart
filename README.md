# Web-Scraping-on-Flipkart
This script scrapes information about mobile phones priced under ₹50,000 from Flipkart and then saves the data in a CSV file. It's pretty neat because it uses libraries like 'requests', 'BeautifulSoup', and 'pandas' to get the job done.

# Web Scraping
Web scraping is all about automatically pulling data from websites with the help of software or scripts. This allows you to access web pages, download the content, and extract the relevant information into a usable format. People use web scraping for all sorts of things like gathering research data, keeping an eye on online prices, and gathering content for websites. However, it's important to always follow the rules and respect the terms of service of the websites you're scraping.

![image](https://github.com/Shreedevi-25/Web-Scraping-on-Flipkart/assets/175317219/c109f568-3433-4ec6-b9eb-8600c4d1720d)

# Flipkart
Flipkart is one of India's largest e-commerce platforms, where you can find a wide range of products including electronics, fashion items, home essentials, books, and more. It started back in 2007 and has since become one of the top online retail stores in India, giving tough competition to global giants like Amazon. Flipkart also operates several subsidiaries and owns cool brands like Myntra and PhonePe, offering services that go beyond traditional online shopping.

# Importing Modules
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Scraping the data from Flipkart
url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

# Request pass to the Flipkart Page
response = requests.get(url)

# To store the web page data in one page
soup = BeautifulSoup(response.content, 'html.parser')

# Scrap the Product name data
title = result.find('div', {'class': 'KzDlHZ'}).text.strip()

# Scrap the Product description data
desc = result.find('div', {'class': '_6NESgJ'}).text.strip()

# Scrap the Product price data
price = result.find('div', {'class': 'Nx9bqj'}).text.strip()

# Scrap the Product review data
review = result.find('div', {'class': 'XQDdHH'}).text.strip()

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('flipkart_mobiles.csv', index=False)

![image](https://github.com/Shreedevi-25/Web-Scraping-on-Flipkart/assets/175317219/61e6b251-7b12-48f4-9134-5920af25f2c4)
