#! /usr/bin/env python
import twitter
import json

consumer_key = '9NP0WklIGcy8pkN1aDNwA'
consumer_secret = 'Hvds4IY08G7JIHoUdIvXXFIqCcLgkyRoICnJjANBOo'
oauth_token = '31194197-MKOMK382pJOtBegFS6Bl2haGPGKUMqINLeUx0bjK6'
oauth_secret = 'VHevRsmuZZuUKWZvCcXHsANCC9dARcafn0GgfR5K8'

auth = twitter.oauth.OAuth(oauth_token, oauth_secret, consumer_key, consumer_secret)

twitter_api = twitter.Twitter(auth=auth)

woe_world = 1
woe_usa = 23424977

world_trends = twitter_api.trends.place(_id=woe_world)
print json.dumps(world_trends)
