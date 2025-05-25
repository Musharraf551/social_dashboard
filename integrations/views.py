from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .twitter_client import fetch_recent_tweets

def twitter_feed_view(request):
    tweets = fetch_recent_tweets(username='musharrafaleem')  # Replace with your own username
    return render(request, 'integrations/twitter_feed.html', {'tweets': tweets})
