#! /usr/bin/env python
import twitter
import json
import os

consumer_key = '0gWw5SAxSBOrKziBM2cQ'
consumer_secret = '736IKboVchX9XTOMPBSQ9tySRY4rmTmZCva9KM8OQNQ'

tilusnet01_creds = os.path.expanduser('~/.twitter/tilusnet01_access')
if not os.path.exists(tilusnet01_creds):
    twitter.oauth_dance("tilusnet-01", consumer_key, consumer_secret,
                tilusnet01_creds)

oauth_token, oauth_secret = twitter.oauth.read_token_file(tilusnet01_creds)

twitter_api = twitter.Twitter(auth=twitter.oauth.OAuth(
    oauth_token, oauth_secret, consumer_key, consumer_secret))


# Get the woe ids from http://isithackday.com/geoplanet-explorer
woe_world = 1
woe_usa = 23424977
woe_uk = 23424975
woe_ita = 23424853
woe_fra = 23424819

trends = twitter_api.trends.place(_id=woe_ita)
print json.dumps(trends)
