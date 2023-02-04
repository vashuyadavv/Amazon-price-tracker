import smtplib

import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP


url ="https://www.amazon.in/DeLonghi-650-85-MS-Primadonna-1450-Watt-Automatic/dp/B07212NJ97/ref=sr_1_1_sspa?" \
     "crid=TOG8PNKLD6I4&keywords=lor+coffee+machine&qid=1669094040&qu=eyJxc2MiOiIyLjEzIiwicXNhIjoiMC4wMCIsInFzcCI6I" \
     "jAuMDAifQ%3D%3D&sprefix=lor+coffee+machin%2Caps%2C198&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/107.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

webpage_contents = response.text

soup = BeautifulSoup(webpage_contents, "lxml")
# print(soup.prettify())

price = float(soup.find(name="span", class_="a-offscreen").getText().split("₹")[1].replace(",", ""))
title = soup.find(name="span", id="productTitle").getText().strip()
# print(price)
# print(title)


BUY_PRICE = 200000

if price < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user="acc70304@gmail.com", password="ivhvqsnporgxpuur")
        connection.sendmail(from_addr="vashu.yadav65@gmail.com",
                            to_addrs="acc70304@gmail.com",
                            msg=f"Subject: Amazon price alert!! \n\n"
                                f"{message}\n {url}")

