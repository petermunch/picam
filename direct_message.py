#!/usr/bin/env python

import twitter
import time
from tweeter import tweet

#Twitter account settings
CONSUMER_KEY = 'sDZ5LCqSBBkqWlSDZeKfQ'
CONSUMER_SECRET = 'YooQn9RQrK2omWvDNdvZteK7R83TQVkSAzHvyl59q4'
ACCESS_KEY = '1653613340-s6Xyr4x2xKQDAOMjkVEOjb4NkBMxtpW89P4nIsF'
ACCESS_SECRET = 'OHeRE5uCcDS81uhmNISYtVHQ7M3MJYpdsLb0bVugU8'
PMU = 31151143

api = twitter.Api(consumer_key='sDZ5LCqSBBkqWlSDZeKfQ',
                    consumer_secret='YooQn9RQrK2omWvDNdvZteK7R83TQVkSAzHvyl59q4',
                    access_token_key='1653613340-mXtzCFnqhh2DTORa1lWJ6LX9Csz35s5njL5HD12',
                    access_token_secret='yWPuv89lueWTFLPSC9eC7RIbtcZraYUxQvoMw3SVEu8J7')


direct_measage = api.GetDirectMessages()


if direct_measage:
    
    id = direct_measage[0].id
    sender = direct_measage[0].sender_screen_name
    text = direct_measage[0].text
    print 'Message from: ', sender
    print 'Message: ', text
    print sender + text

    if direct_measage[0].sender_id == PMU:
        
        if direct_measage[0].text == 'snapshot' or direct_measage[0].text == 'Snapshot':
            
            tweet()
            api.DestroyDirectMessage(id)
            print 'Picture Tweetet - Message deleted...'
            
        elif direct_measage[0].text == 'test' or direct_measage[0].text == 'Test':
            
            api.DestroyDirectMessage(id)
            print 'Testing purpose only - Message deleted...'
        
        else:
            api.DestroyDirectMessage(id)
            api.PostUpdate('Message format wrong - Message deleted')
            print 'Message format not correct'
    else:
        tweet = 'Unorthorized message from: ', sender + 'Text: ', text
        print tweet
        
        api.DestroyDirectMessage(id)
        api.PostUpdate('Message not from PM - Message deleted')
        print 'Message not from PM - Message deleted'
        
else:
    
    print 'No New Message, sorry'



