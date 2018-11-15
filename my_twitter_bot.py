import tweepy
import time

FILE_NAME = 'last_seen.txt'
print('My twiter bot')

CONSUMER_KEY = '<enter consumer_key here>'
CONSUMER_SECRET = '<enter consumer_secret here>'
ACCESS_KEY = '<enter access_key here>'
ACCESS_SECRET = '<enter access_secret here>'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def retrieve_last_seen_id(filename):
    f_read = open(filename, 'r')
    last_seen_id = f_read.read()
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, filename):
    f_write = open(filename, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweet():
    # DEV NOTE- use 1063097217945296896 for testing from beginning
    mentions = []
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    print('Last seen id={}'.format(last_seen_id))
    if last_seen_id != '' and last_seen_id != None:
        mentions = api.mentions_timeline(last_seen_id)
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        #print(str(mention.id) + ' -- ' + mention.text)
        if '#okaysidd' in mention.text.lower():
            print('Found #okaysidd    responding...\n')
            api.update_status('@' + mention.user.screen_name + ' test successful :) How did you find us?', mention.id)
            print('Responded to tweet -- {}'.format(mention.text))

print('Starting to retrieve tweets after the last checked tweet, and replying to those with #okaysidd in them.')
while 1:
    reply_to_tweet()
    time.sleep(60)
