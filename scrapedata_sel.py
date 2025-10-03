from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

data=[]
options=webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument("--window-size=1200,800")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
for i in range(2,5):

    url=f"https://www.flipkart.com/search?q=phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    driver.get(url) 

    products = driver.find_elements(By.CSS_SELECTOR, "div.cPHDOP")  # main product containers
    
    for product in products:
        try:
            name_el = product.find_element(By.CSS_SELECTOR, "div.KzDlHZ")  # product link contains name
            price_el = product.find_element(By.CSS_SELECTOR, "div.Nx9bqj._4b5DiR")
            rating = product.find_element(By.CSS_SELECTOR,"div.XQDdHH")  # price
            name = name_el.text.strip()
            price = price_el.text.strip().replace("₹", "").replace(",", "")
            rate=rating.text.strip()  # trim ₹ and commas
            data.append({"name": name, "price": int(price),"rating":rate})
        except:
            pass # skip containers without products
driver.quit()

# Show results
for d in data:
    print(d)

# Optional: Save to CSV
df = pd.DataFrame(data)
df.to_csv("flipkart_products.csv", index=False, encoding="utf-8")