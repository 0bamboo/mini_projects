from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#the path for webdriver in my laptop:
# path = '/home/mugiwara/chromedriver.exe'
#the path for chromedriver in imac:
path = '/Users/abdait-m/Cdriver/chromedriver'
try:
    driver = webdriver.Chrome(path)
    driver.get('https://bandcamp.com')
    driver.maximize_window()
    play_button = driver.find_element_by_class_name('playbutton')
    play_button.click()
    tracks = driver.find_elements_by_class_name('discover-item')
    print(len(tracks))
    counter = 1
    # for item in range(len(tracks)):
    #     tracks[item].click()
    #     time.sleep(2)
    # tracks[3].click()
    for elem in driver.find_elements_by_class_name('item-page'):
        print(elem.text.lower().find('next'))
        if elem.text.lower().find('next') == 0:
            print(elem.text.lower().find('next'))
            next_button = elem
    next_button.click()
    time.sleep(5)
    tracks = driver.find_elements_by_class_name('discover-item')
    print(len(tracks))
    tracks[9].click()
    # assert len(tracks) == 8
    # for item in range(8 * counter, len(tracks)):
    #     tracks[item].click()
    #     time.sleep(2)
    next_button = [elem for elem in driver.find_elements_by_class_name('item-page') if elem.text.lower().find('next') > -1]
    next_button[0].click()
    time.sleep(5)
    tracks = driver.find_elements_by_class_name('discover-item')
    counter += 1
    print(len(tracks))
    # for item in range(8 * counter, len(tracks)):
    #     tracks[item].click()
    #     time.sleep(2)
    print(f'|{tracks[17]}|')
    tracks[17].click()
    print(type(next_button))

except:
    print('\n ERROR OCCURRED \n')
finally:
    time.sleep(10)
    driver.quit()