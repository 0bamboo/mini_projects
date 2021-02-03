from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from collections import namedtuple
from threading import Thread
from os.path import isfile
import csv


BAND_CAMP_LINK = 'https://bandcamp.com/'
PATH = '/Users/abdait-m/Cdriver/chromedriver'


class Band_Camp_Player():
    
    def __init__(self):
        # Create the browser
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(BAND_CAMP_LINK)

        # Track list related state
        self.current_track_nbr = 1
        self.track_list = []
        self.tracks()
        self.play()
        self.play_next()
        self.exit()

    
    def tracks(self):
        '''
            Get the data of tracks available .
        '''
        # Sleep to give the browser time to render and finish any animations
        sleep(2)

        # Get the container for the visible track list
        discover_section = self.driver.find_element_by_class_name('discover-results')
        left_x = discover_section.location['x']
        right_x = discover_section.size['width'] + left_x
        # print(discover_section.size['width'])

        # Filter the items in the list to include ony those we can click
        discover_items = self.driver.find_elements_by_class_name('discover-item')
        self.track_list = [item for item in discover_items if item.location['x'] >= left_x and item.location['x'] < right_x]

        # Print the available tracks to the screen
        for (i, track) in enumerate(self.track_list):
            print(f'[The track : {i + 1}]')
            lines = track.text.split('\n')
            print(f'Album : {lines[0]}')
            print(f'Artist : {lines[1]}')
            if len(lines) > 2:
                print(f'Genre : {lines[2]}')
    

    def catalogue_pages(self):
        '''
            Print the available pages in the catalogue that are presently accessible .
        '''

        print('PAGES')
        for page in self.driver.find_elements_by_class_name('item-page'):
            print(page.text)
        print()


    def more_tracks(self, page = 'next'):
        ''' 
            Advances the catalogue and repopulates the track list. to advance any of available pages.
        '''
        next_btn = [item for item in self.driver.find_elements_by_class_name('item-page') if item.text.lower().strip() == str(page)]

        # Or try this :
        # for item in self.driver.find_elements_by_class_name('item-page'):
        #   if item.text.lower().find('next') == 0:
        #       next_btn = item  

        if next_btn:
            next_btn[0].click()
            self.tracks()
        

    def play(self, track = None):
        '''
            Play a track. If no track number is supplied, the presently will play.
        '''

        if track is None:
            self.driver.find_element_by_class_name('playbutton').click()
        elif type(track) is int and track <= len(self.track_list) and track >= 1:
            self.current_track_nbr = track
            self.track_list[self.current_track_nbr - 1].click()
    

    def play_next(self):
        '''
        Plays the next 
        '''
        if self.current_track_nbr < len(self.track_list):
            self.play(self.current_track_nbr + 1)
        else:
            self.more_tracks()
            self.current_track_nbr = 0
            self.play(self.current_track_nbr + 1)
    

    # def play_each_song_for_little_bit_then_skip(self, time = 10, how_many_songs = 1):
    #     '''
    #         This function is for playing some songs for little bit of time , You get to choose how many seconds to play for a song ,
    #         and how many songs you want to listen to . the first argument is for how many seconds for each song , and the second argument is for how many songs you want to listen to.
    #     '''
    #     try:
    #         for song in range(how_many_songs):
    #             print(f'**************{song}*************')
    #             if song == 0:
    #                 self.play()
    #                 sleep(time)
    #                 continue
    #             self.play_next()
    #             sleep(time)
    #     except Exception as exc:
    #         print(f'ERROR OCCURRED : {exc}')
    #     finally:
    #         self.exit()


    def pause(self):
        ''' 
        Pause the playback
        '''
        self.play()

    
    def exit(self):
        sleep(3)
        self.driver.quit()
    


if __name__ == '__main__':
    print(__name__)
    try:
        test = Band_Camp_Player()
        # test.play_each_song_for_little_bit_then_skip(10, 3)
        test.play()
        for i in range(5,10):
            sleep(2)
            test.play_next() # something wrong with this function try to fix the error 
            if i == 5:
                test.pause()
    except Exception as exc:
        sleep(2)
        print(f'ERROR OCCURRED : {exc}')
    # test.exit()
else:
    print('Your not running the original file')