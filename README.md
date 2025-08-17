# 🛒 Amazon Price Alert  

A simple Python script that tracks product prices on Amazon and sends you an email alert when the price drops below your desired threshold.  

---

## 📌 Features  
- Scrapes product details and current price from Amazon  
- Sends an email notification when the price falls below the set limit  
- Secure credentials management with `.env` file  

---

## 🚀 How It Works  
1. The script fetches the Amazon product page using `requests`  
2. It parses the price and product title with **BeautifulSoup + lxml**  
3. If the price is below your target (default: `$100`), it sends an email alert via **SMTP**  

---

## 🛠️ Requirements  
- Python 3.8+  
- Install dependencies:  
  ```bash
  pip install requests beautifulsoup4 lxml python-dotenv
