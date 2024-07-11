import pandas as pd
import requests
from bs4 import BeautifulSoup

# Initialize an empty list to store the data
data = []

# URL of the Flipkart search page
for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the search results
    search_results = soup.find_all('div', {'class': 'tUxRFH'})

    # Iterate over the search results
    for result in search_results:
        try:
            # Extract the product name
            title = result.find('div', {'class': 'KzDlHZ'}).text.strip()

            # Extract the product description
            desc = result.find('div', {'class': '_6NESgJ'}).text.strip()

            # Extract the product price
            price = result.find('div', {'class': 'Nx9bqj'}).text.strip()

            # Extract the product review
            review = result.find('div', {'class': 'XQDdHH'}).text.strip()

            # Append the data to the list
            data.append({
                'Title': title,
                'Description': desc,
                'Price': price,
                'Review': review
            })
        except AttributeError:
            # If any attribute is missing, skip this product
            continue

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('flipkart_mobiles.csv', index=False)

print("Data saved to flipkart_mobiles.csv")