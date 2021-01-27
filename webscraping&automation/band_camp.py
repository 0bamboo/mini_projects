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
    discover_section = driver.find_element_by_class_name('discover-results')
    print(discover_section.location)
    for elem in driver.find_elements_by_class_name('item-page'):
        if elem.text.lower().find('next') == 0:
            next_button = elem
    next_button.click()
    time.sleep(5)
    # tracks = driver.find_elements_by_class_name('discover-item')
    # print(len(tracks))
    # THIS IS THE METHOD TO FILTER THE LIST OF TRACKS WHEN YOU PRESS NEXT BUTTON 
    discover_section = driver.find_elements_by_class_name('discover-results')
    print('1')
    print('2')
    #  WE USE THE METHOD LOCATION TO FIND THE COORDINATES OF DISCOVER SECTION THE RETURN VALUE IS A DICT {'x': xcoor, 'y': ycoor}
    print(discover_section[0].location['x'])
    print('3')
    left_x = discover_section[0].location['x']
    print('4')
    right_x = left_x + discover_section[0].size['width']
    discover_items = driver.find_elements_by_class_name('discover-item')
    tracks = list()
    print(type(discover_items))
    for item in discover_items:
        if item.location['x'] >= left_x and item.location['x'] < right_x:
            tracks.append(item)
    print('im here')
    tracks[0].click()
    print(len(tracks))


    # tracks[9].click()
    # assert len(tracks) == 8
    # for item in range(8 * counter, len(tracks)):
    #     tracks[item].click()
    #     time.sleep(2)
    # next_button = [elem for elem in driver.find_elements_by_class_name('item-page') if elem.text.lower().find('next') > -1]
    # next_button[0].click()
    # time.sleep(5)
    # tracks = driver.find_elements_by_class_name('discover-item')
    # counter += 1
    # print(len(tracks))
    # for item in range(8 * counter, len(tracks)):
    #     tracks[item].click()
    #     time.sleep(2)
    # print(f'|{tracks[17]}|')
    # tracks[17].click()
    # print(type(next_button))

# except:
#     print('\n ERROR OCCURRED \n')
finally:
    time.sleep(10)
    driver.quit()