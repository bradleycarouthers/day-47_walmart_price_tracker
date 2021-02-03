import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = YOUR_EMAIL
MY_PASSWORD = YOUR_PASSWORD
url = "https://www.walmart.com/ip/HP-20kd-LED-monitor-19-5-19-5-viewable-1440-x-900-IPS-250-cd-m-1000-1-8-ms-DVI-D-VGA-black/525425410"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(
    url=url,
    headers=header
)

soup = BeautifulSoup(response.content, "lxml")

# Find the dollar and cent value, combine them as strings and turn into float
dollar_val = soup.find("span", class_="price-characteristic").getText()
cent_val = soup.find("span", class_="price-mantissa").getText()
price = float(dollar_val + "." + cent_val)
print(price)
title = soup.find(
    "h1",
    class_="prod-ProductTitle prod-productTitle-buyBox font-bold").getText()

# Email sent if condition True
if price < 200.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="baadstar@gmail.com",
            msg=f"Subject:Low Price Alert For...\n\n{title}, is now ${price}.\nPurchase now at: {url}"
        )
