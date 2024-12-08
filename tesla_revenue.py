import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://companiesmarketcap.com/tesla/revenue/"  # Replace with the actual URL
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Example extraction logic
table = soup.find("table")  # Adjust based on the site structure
data = []
for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    data.append([col.text.strip() for col in cols])

tesla_revenue = pd.DataFrame(data, columns=["Year", "Revenue", 'Change'])
tesla_revenue.to_csv("tesla_revenue_data.csv", index=False)  # Save for sharing
print(tesla_revenue.head())  # Display the first few rows
