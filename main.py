from bs4 import BeautifulSoup
import lxml
import os
from dotenv import load_dotenv
import requests
import smtplib
load_dotenv()
email = os.getenv("email")
password = os.getenv("password")
receiver = os.getenv("receiver_email")
smtp_address = os.getenv("smtp_address")
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",headers=headers)
text = response.text
soup = BeautifulSoup(text, "lxml")
price = float(soup.find(name="span", class_= "a-price-whole").text) + float("0."+soup.find(name="span",class_= "a-price-fraction").text)
product = soup.find(name="span", id= "productTitle").text
#
product_title = " ".join(product.split())
try:
    if price < 100:
        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(email,password)
            connection.sendmail(from_addr=email, to_addrs=receiver, msg=f"Subject:Discount Price Alert!\n\n{product_title} is now ${price}".encode("utf-8"))
            print("successfully send the email")

except Exception as e:
    print(f"Sorry there was an error: {e}")