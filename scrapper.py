import requests
from bs4 import BeautifulSoup

keyword="파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

soup.find_all()