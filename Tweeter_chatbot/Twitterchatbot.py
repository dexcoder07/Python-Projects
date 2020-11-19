#importing Libraries

import tweepy as twt
import time

#Accessing the API module of Tweeter
CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXX'

CONSUMER_SECRET = 'XXXXXXXXXXXXXXXX'

ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

try:
    auth = twt.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = twt.API(auth)
except:
    print("Error Occured")

FILE_NAME = 'visit_id.txt'

last_liked = 12345

#Retreiving the Last seen File

def retrieve_last_seen_id(file_name):
    try:
        f_read = open(file_name, 'r')

        last_seen_id = int(f_read.read().strip())

        f_read.close()
    except:
        print("Error reading file")

    return last_seen_id

#Storing the ID of last replyed

def store_last_seen_id(last_seen_id, file_name):
    try:
        f_write = open(file_name, 'w')

        f_write.write(str(last_seen_id))

        f_write.close()
    except IOError:
        print("Can't Find File")

    return

#Liking the tweet on home page

def like():
    tweets = api.home_timeline(count=1)
    global last_liked
    tweet = tweets[0]
    if(last_liked!= tweet.id):
        print(f"Liking tweet {tweet.id} of {tweet.author.name}")
        api.create_favorite(tweet.id)
        last_liked = tweet.id
        print("Tweet Liked")
    else:
        print("Already Liked ID")

#Replying to the tweets on the timeline

def reply():
    print("retreving the tweet and replying")

    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(last_seen_id,tweet_mode = 'extended')

    for mention in reversed(mentions):
         print(mention.id,"-",mention.text)
         last_seen_id = mention.id
         store_last_seen_id(last_seen_id,FILE_NAME)
         if('hello' in mention.text.lower()):
             print("replying to: ",mention.user.screen_name)
             api.update_status('@'+mention.user.screen_name+" Hey!!!",mention.id)

#Checking for the follow request and doing followback

def follow_back():
    for follower in twt.Cursor(api.followers).items():
        follower.follow()
        print(follower.screen_name)

while True:

    try:
        reply()

        print("Checking for follow request and doing follow back")
        follow_back()

        print("Liking the tweets")
        like()
        api.rate_limit_status()
        time.sleep(15)

    except twt.RateLimitError:
        print("Rate Limit ")
