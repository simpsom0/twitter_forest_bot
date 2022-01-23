import tweepy

consumer_key = "placeholder"
consumer_secret = "placeholder"
access_token = "placeholder"
access_token_secret = "placeholder"

def make_tweet(message):
    # oauth = OAuth()
    # api = tweepy.API(oauth)

    # posts tweet
    # api.update_status(message)

    print(message)


# credit: https://www.youtube.com/watch?v=0FOUFF4q14A
def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None