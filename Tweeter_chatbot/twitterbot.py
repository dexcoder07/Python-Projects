# importing Libraries

import tweepy as twt
import time

# Accessing the API module of Tweeter

CONSUMER_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

CONSUMER_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

ACCESS_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'

try:
    auth = twt.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = twt.API(auth)
except twt.TweepError as error:
    print("Error Connecting")

# Opening file to store the ID of replied person
FILE_NAME = 'visit_id.txt'

# Getting Username
screen_name = api.me().screen_name

# Retrieving the Last seen File


def retrieve_last_seen_id(file_name):
    try:
        f_read = open(file_name, 'r')

        last_seen_id = int(f_read.read().strip())

        f_read.close()
    except IOError:
        print("Error reading file")

    return last_seen_id

# Storing the ID of last replied


def store_last_seen_id(last_seen_id, file_name):
    try:
        f_write = open(file_name, 'w')

        f_write.write(str(last_seen_id))

        f_write.close()

    except IOError:
        print("Can't Find File")

    return


# Liking the tweet on home page


def like():
    print("Liking the tweets")

    tweets = api.home_timeline(count=1)

    tweet = tweets[0]

    try:
        print(f"Liking tweet {tweet.author.name}")
        api.create_favorite(tweet.id)
        print("Tweet Liked")
    except twt.TweepError:
        print("DONE...")

# Replying to the tweets on the timeline


def reply():
    print("retrieving the tweet and replying")

    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
         print(mention.id,"-",mention.text)
         last_seen_id = mention.id
         store_last_seen_id(last_seen_id,FILE_NAME)
         if 'hello' in mention.text.lower():
             print("replying to: ",mention.user.screen_name)
             api.update_status('@'+mention.user.screen_name+" Hey!!!",mention.id)
         if '#Hello' in mention.text.lower():
            print("replying to: ", mention.user.screen_name)
            api.update_status('@' + mention.user.screen_name + "#Hey!!!", mention.id)

# Checking for the follow request and doing follow back


def follow_back():
    print("Checking for follow request and doing follow back")
    global screen_name

    l = []

# getting the list of people whom I was following

    for friend in twt.Cursor(api.friends).items():
        l.append(friend.screen_name)

# checking if the person in following is being followed back
    for follower in twt.Cursor(api.followers).items():
        if follower.screen_name not in l:
            follower.follow()
            print("New Follower: "+follower.screen_name)



while True:

    try:
        reply()

        follow_back()

        like()

        api.rate_limit_status()

        time.sleep(15)

    except twt.RateLimitError as Er:
        print(Er)
