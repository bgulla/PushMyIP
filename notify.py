import tweepy, sys,os

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def tweet(msg, ):
    consumer_key = os.environ.get('twitter_consumer_key')
    consumer_secret = os.environ.get('twitter_consumer_secret')
    access_token = os.environ.get('twitter_access_token')
    access_token_secret = os.environ.get('twitter_token_secret')
    notify_host = os.environ.get('HOST', 'defaulthost')
    if all(v is not None for v in [A, B, C, D, E]):
        print
    else:
        fail

def send_tweet(msg, consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    print "Successfully logged in as " + api.me().name + "."
    try:
     if msg <= 140:
      api.update_status(msg)
      print "Successfully tweeted: " + "'" + sys.argv[1] + "'!"
     else:
      raise IOError
    except:
     print "Something went wrong: either your tweet was too long or you didn't pass in a string argument at launch."
    finally:
     print "Shutting down script..."