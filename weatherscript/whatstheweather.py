
import requests
from bs4 import BeautifulSoup



source = requests.get('http://www.google.com').text
atr = BeautifulSoup(source, 'lxml')
article = atr.find('div', id = 'guser')
print(article.a.text)
