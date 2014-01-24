#!/usr/bin/env python
import sys
import os
from twython import Twython
import twitter

#Twitter account settings
CONSUMER_KEY = 'sDZ5LCqSBBkqWlSDZeKfQ'
CONSUMER_SECRET = 'YooQn9RQrK2omWvDNdvZteK7R83TQVkSAzHvyl59q4'
ACCESS_KEY = '1653613340-mXtzCFnqhh2DTORa1lWJ6LX9Csz35s5njL5HD12'
ACCESS_SECRET = 'yWPuv89lueWTFLPSC9eC7RIbtcZraYUxQvoMw3SVEu8J7'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

def tweet(filename):
    #Use raspistill to take the photo
    #os.system("raspistill -o image.jpg -w 640 -h 480 -q 50")

    # Feed the photo to Twitter
    print filename
    photo = open('filename','rb')
    api.update_status_with_media(media=photo, status='RaspberryPi Opdaterer:')

#if __name__ == '__main__':
    # test1.py executed as script
    # do something
    #tweet()
    
