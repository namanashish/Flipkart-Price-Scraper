import requests
import pandas as pd
from bs4 import BeautifulSoup
data=[];
url="";
for i in range (1,3):
    url=f"https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
    response=requests.get(url,headers)
    soup=BeautifulSoup(response.content,"html.parser")

    products=soup.select("div.tUxRFH")
    for product in products:
        prod=product.select_one("div.KzDlHZ")
        k={}
        if prod:
            nam = prod.text.strip()
            k['name']=nam
            print(nam)

        prod = product.select_one("div.Nx9bqj._4b5DiR")
 
        if prod:
           price=prod.text.strip()
           trimmed_price = price.replace("₹", "")
           k['price']=trimmed_price
           print(trimmed_price)

        prod = product.select_one("div.XQDdHH")
        if prod:
           
           rate=prod.text.strip()
           k["rating"]=rate
           print(rate)

        data.append(k)

df=pd.DataFrame(data);
df.to_csv(r"C:\Users\naman\Downloads\prac\data\flip_laptop3.csv")