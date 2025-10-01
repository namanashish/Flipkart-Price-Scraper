# Flipkart Laptop Price Scraper

## Problem Statement

Extract data from Flipkart in order to **keep track of laptop prices**.

---

## Resources

* Flipkart website
* BeautifulSoup

---

## Steps

### Step 1: Detect Product Containers

Works without automation.
Inspect the page to detect the **classes which contain all the products**.

* In this case, `tUxRFH` contains all the products.

### Step 2: Extract Name, Price, and Rating

* Name, Price, and Rating are contained in `<div>` elements.
* Select each one individually and extract the text.

### Step 3: Handle Headers and Price Symbol

```python
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
```

* The price contains the **Rupee symbol (₹)** which can be difficult to parse.
* Remove or handle it separately for numeric storage.

### Step 4: Store Data

* Append the extracted **name, price, and rating** into a **dictionary-like structure** for easy handling.

### Step 5: Convert to CSV

* Convert the final data into a **CSV file** for further use.

---

## Output

* Data shape: **24 × 3** (24 products, 3 attributes each)
* CSV file will contain columns: `Name`, `Price`, `Rating`

---

## Sample Python Code

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

url = 'https://www.flipkart.com/search?q=laptops'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_='tUxRFH')
data = []

for product in products:
    try:
        name = product.find('div', class_='product-name-class').text.strip()
        price = product.find('div', class_='product-price-class').text.strip().replace('₹', '').replace(',', '')
        rating = product.find('div', class_='product-rating-class').text.strip()
        data.append({'Name': name, 'Price': price, 'Rating': rating})
    except:
        continue

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('flipkart_laptops.csv', index=False, encoding='utf-8')
```
