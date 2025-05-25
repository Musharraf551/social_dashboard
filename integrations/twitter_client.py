import tweepy
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

# Get Twitter API credentials
API_KEY = os.getenv('TWITTER_API_KEY')
API_SECRET = os.getenv('TWITTER_API_SECRET')
ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def fetch_recent_tweets(username, count=5):
    """
    Fetches the latest tweets from a user timeline.
    """
    try:
        tweets = api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
        return [{"text": tweet.full_text, "created_at": tweet.created_at} for tweet in tweets]
    except Exception as e:
        print("Error fetching tweets:", e)
        return []
