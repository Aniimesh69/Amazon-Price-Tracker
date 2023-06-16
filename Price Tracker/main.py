import requests
from bs4 import BeautifulSoup
import lxml

#url = "https://www.amazon.in/Apple-11-inch-iPad-Pro-Wi-Fi-128GB/dp/B0BJLFBYV1/"

url = "https://www.amazon.in/Sony-PS5-PlayStation-Console/dp/B0BRCP72X8/"

#url = "https://www.amazon.in/Apple-iPhone-Mini-512GB-Starlight/dp/B09G98Z83G/"

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers = headers)

    soup = BeautifulSoup(r.text, "lxml")

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    uc_price = soup.select_one(selector=".a-price-whole").getText()
    def clean_string(s):
        cleaned = ''.join(filter(lambda x: x.isdigit() or x == '.', s))
        return float(cleaned)

    s = uc_price
    price = clean_string(s)
    
    return name, price

print(get_link_data(url))

