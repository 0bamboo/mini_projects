
import requests
from bs4 import BeautifulSoup



page = requests.get("https://weather.com/weather/today/l/1078e192cff707be1411900bb06026d9eda1d6f65ad88eb396da69cf08fd1abe").text
soup = BeautifulSoup(page, "html.parser")
# print(soup.find(class_ = "card Card--cardPadded--2jAM0 Card--card--4VS_Q CurrentConditions--card--1sxFO gradients--sunnyDay-contrast--3BFuJ CurrentConditions--gradient--2g3vw"))
city = soup.find("div", class_ = 'CurrentConditions--header--3-4zi').h1.text
city = city.split(',')[0]
time = soup.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[2]
weather = soup.find('span', class_ = 'CurrentConditions--tempValue--3KcTQ').text
mornight = soup.find('div', class_ = 'CurrentConditions--tempHiLoValue--A4RQE')
print(mornight)
print(weather)
print(city)
print(time)
