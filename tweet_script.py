import tweepy
from time import sleep

#Setup your twitter dev account on https://developer.twitter.com/
#to know more read this blog https://docs.inboundnow.com/guide/create-twitter-application/

CONSUMER_KEY = '***'
CONSUMER_SECRET = '****'
ACCESS_KEY = '***'
ACCESS_SECRET = '***'

print('Script started')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user_names = open('user_names.txt', 'r').read().splitlines()
for user_name in user_names:
    tweet = '@' + user_name + ' Otomatik mention metni'
    print('Tweeting "{}"'.format(tweet))
    api.update_status(tweet)
    sleep(60)
