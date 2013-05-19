#! /usr/bin/env python
import twitter
import json
import os


def read_token_file(filename):
    f = open(filename)
    return f.readline().strip(), f.readline().strip()


tilusnet01_consumer_creds = os.path.expanduser('~/.twitter/tilusnet01_consumer_creds')
tilusnet01_token_creds = os.path.expanduser('~/.twitter/tilusnet01_token_creds')
consumer_key, consumer_secret = read_token_file(tilusnet01_consumer_creds)

if not os.path.exists(tilusnet01_token_creds):
    twitter.oauth_dance("tilusnet-01", consumer_key, consumer_secret,
                tilusnet01_token_creds)

oauth_token, oauth_secret = twitter.oauth.read_token_file(tilusnet01_token_creds)

twitter_api = twitter.Twitter(auth=twitter.oauth.OAuth(
    oauth_token, oauth_secret, consumer_key, consumer_secret))


# Get the woe ids from http://isithackday.com/geoplanet-explorer
woe_world = 1
woe_usa = 23424977
woe_uk = 23424975
woe_ita = 23424853
woe_fra = 23424819
woe_tm = 881802

trends = twitter_api.trends.place(_id=woe_fra)
print json.dumps(trends)
