import requests
from bs4 import BeautifulSoup


def _get_weather():
    page = requests.get("https://weather.com/weather/today/l/1078e192cff707be1411900bb06026d9eda1d6f65ad88eb396da69cf08fd1abe").text
    soup = BeautifulSoup(page, "html.parser")
    # print(soup.find(class_ = "card Card--cardPadded--2jAM0 Card--card--4VS_Q CurrentConditions--card--1sxFO gradients--sunnyDay-contrast--3BFuJ CurrentConditions--gradient--2g3vw"))
    city = soup.find("div", class_ = 'CurrentConditions--header--3-4zi').h1.text
    city = city.split(',')[0]
    time = soup.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[2] + ' ' + soup.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[3]
    weather = int(soup.find('span', class_ = 'CurrentConditions--tempValue--3KcTQ').text[:-1])
    weather = (weather - 32) * 5//9
    if weather < 13:
        feel = 'cold'
    elif weather >= 13 and weather <= 30:
        feel = 'normal'
    else:
        feel = 'hot'
    weather = str(weather) + ' °C'
    print(f"""\033[1;32;40m
            THE WEATHER TODAY IN {city} AT {time}:
        \033[1;36;40m
        The tempeture is {weather} , it's {feel}
    """)

if __name__ == '__main__':
    _get_weather()
