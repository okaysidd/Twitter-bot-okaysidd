import tweepy
import time

FILE_NAME = 'last_seen.txt'
print('My twiter bot')

CONSUMER_KEY = 'lsmZwSPdLjkKjF3lAoslYFoKP'
CONSUMER_SECRET = '22poxBoxPWzfvRBYWaM4uuwC9UuaxFVQinfgM4PPpgvqWrgt44'
ACCESS_KEY = '1062705651745345537-krviZj55FHDIlmq0MZfyV2kC8g9s2H'
ACCESS_SECRET = 'N2GOQnZuHS39JPj5hPOmTDIkpPlUGGLWrlj4qtv5T5M3w'

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
    # DEV NOTE- use 1062755960848969729 for testing from beginning

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
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
