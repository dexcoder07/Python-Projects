# importing Libraries

import tweepy as twt
import time

# Accessing the API module of Tweeter

CONSUMER_KEY = '6GtuOXXXXXXXXXXXXXXXXXXXXXX'

CONSUMER_SECRET = 'PPcSjYXXXXXXXXXXX'

ACCESS_KEY = '9385XXXXXXXXXXXXXXXXXXXXXX'

ACCESS_SECRET = '5i1NXXXXXXXXXXXXXXXXXXXXXX'

#Connecting with TWITTER API

try:
    auth = twt.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = twt.API(auth)
except twt.TweepError:
    print("Error Connecting")


screen_name = api.me().screen_name


# Liking the tweet on home page


def like():
    print("Liking the tweets")

    tweets = api.home_timeline(count=1)


    tweet =tweets[0]

    try:
        print(f"Liking tweet {tweet.author.name}")
        api.create_favorite(tweet.id)
        #store_last_seen_id(tweet.id, Likes_id)
        print("Tweet Liked")
    except twt.TweepError:
        print("DONE...")


# Replying to the tweets on the timeline


def reply():
    print("retrieving the tweet and replying")

    mentions = api.mentions_timeline()

    for mention in reversed(mentions):
       print(mention.id,"-",mention.text)
       try:
           if 'hello there!!!' in mention.text.lower():
               print("replying to: ",mention.user.screen_name)
               api.update_status('@'+mention.user.screen_name+" Hello "+mention.user.screen_name+"!!!",mention.id)
           elif ('how are you?' or 'how are you') in mention.text.lower():
              print("replying to: ", mention.user.screen_name)
              api.update_status('@' + mention.user.screen_name + " Hey i am good, how are you?", mention.id)
           elif '#StaySafe' in mention.text.lower():
               print("replying to: ", mention.user.screen_name)
               api.update_status('@' + mention.user.screen_name + "#You Too", mention.id)
           elif '#StayHome' in mention.text.lower():
               print("replying to: ", mention.user.screen_name)
               api.update_status('@' + mention.user.screen_name + "#You Too", mention.id)
           else:
               print("No replies")
       except:
           print("Replied")

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

        api.rate_limit_status()
        reply()

        follow_back()

        like()

        time.sleep(15)

    except twt.RateLimitError:
        print("Continue.....")
