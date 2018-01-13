import tweepy, sys,os
from pushbullet import Pushbullet

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


def pushb(msg):
    pushbullet_key = os.environ.get("PUSHBULLET_KEY").replace('"','')
    pb = Pushbullet(pushbullet_key)
    msg = "[%s] %s" % (os.environ.get('HOST', 'defaulthost'), msg)
    pb.push_note("PushMyIP", msg)



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