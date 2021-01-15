import requests
from bs4 import BeautifulSoup

def feel_(weather):
    if weather < 13:
        feel = 'cold'
    elif weather >= 13 and weather <= 30:
        feel = 'normal'
    else:
        feel = 'hot'
    return feel

def get_the_weather_of_aoulouz():
    page_aou = requests.get("https://weather.com/weather/today/l/4a9d4feb11fc2d44128a3795e9c45b2c058069894ae02867bd7cc2de9267f689").text
    soup_aou = BeautifulSoup(page_aou, "html.parser")
    city_aou = soup_aou.find("div", class_ = 'CurrentConditions--header--3-4zi').h1.text.split(',')[0]
    time_aou = soup_aou.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[2] + ' ' + soup_aou.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[3]
    weather_aou = (int(soup_aou.find('span', class_ = 'CurrentConditions--tempValue--3KcTQ').text[:-1]) - 32) * 5//9
    feel_aou = feel_(weather_aou)
    weather_aou = str(weather_aou) + ' °C'
    print(f"""\033[1;32;40m
            THE WEATHER TODAY IN {city_aou}
        \033[1;36;40m
         AT {time_aou}, The tempeture is {weather_aou} , it's {feel_aou}
    """)


def get_the_weather_of_agadir():
    page_aga = requests.get("https://weather.com/weather/today/l/948bb88aa0a196ed67b20b1ab874927f1fa6d0c8bf68528a8755d18f26b9496c").text
    soup_aga = BeautifulSoup(page_aga, "html.parser")
    city_aga = soup_aga.find("div", class_ = 'CurrentConditions--header--3-4zi').h1.text.split(',')[0]
    time_aga = soup_aga.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[2] + ' ' + soup_aga.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[3]
    weather_aga = (int(soup_aga.find('span', class_ = 'CurrentConditions--tempValue--3KcTQ').text[:-1]) - 32) * 5//9
    feel_aga = feel_(weather_aga)
    weather_aga = str(weather_aga) + ' °C'
    print(f"""\033[1;32;40m
            THE WEATHER TODAY IN {city_aga}
        \033[1;36;40m
         AT {time_aga}, The tempeture is {weather_aga} , it's {feel_aga}
    """)


def get_the_weather_of_khouribga():
    page_khou = requests.get("https://weather.com/weather/today/l/1078e192cff707be1411900bb06026d9eda1d6f65ad88eb396da69cf08fd1abe").text
    soup_khou = BeautifulSoup(page_khou, "html.parser")
    city_kh = soup_khou.find("div", class_ = 'CurrentConditions--header--3-4zi').h1.text.split(',')[0]
    time_kh = soup_khou.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[2] + ' ' + soup_khou.find('div', class_ = "CurrentConditions--timestamp--1SWy5").text.split()[3]
    weather_kh = (int(soup_khou.find('span', class_ = 'CurrentConditions--tempValue--3KcTQ').text[:-1]) - 32) * 5//9
    feel_kh = feel_(weather_kh)
    weather_kh = str(weather_kh) + ' °C'
    print(f"""\033[1;32;40m
            THE WEATHER TODAY IN {city_kh}
        \033[1;36;40m
         AT {time_kh}, The tempeture is {weather_kh} , it's {feel_kh}
    """)


def description_function():
    print("""\033[1;33;40m

            This a simple script for getting ,
            the weather in three different cities in morocco.

            The cities are KHOURIBGA, AGADIR and AOULOUZ.

            Just type the city name that you want 
            to know its weather and you will get it or type all,
            for getting the weather in the three cities.

            Else if you're not interested type exit to exit.

            ENJOY :)
            \033[0;37;40m
    """)


def _get_weather(which_city):
    if which_city.lower() == 'all':
        get_the_weather_of_aoulouz()
        get_the_weather_of_agadir()
        get_the_weather_of_khouribga()
    elif which_city.lower() == 'agadir':
        get_the_weather_of_agadir()
    elif which_city.lower() == 'aoulouz':
        get_the_weather_of_aoulouz()
    elif which_city.lower() == 'khouribga':
        get_the_weather_of_khouribga()


if __name__ == '__main__':
    description_function()
    which_city = input('\033[2;37;40m Enter the name of the city : \033[0;37;40m')
    if which_city == "exit":
        exit()
    while which_city.lower() not in ["agadir", "khouribga", "aoulouz", "all"]:
        which_city = input('\033[2;37;40m Enter the name of the city : \033[0;37;40m')
        if which_city == 'exit':
            exit()
    _get_weather(which_city)
