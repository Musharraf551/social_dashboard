from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .twitter_client import fetch_recent_tweets

from django.core.cache import cache

def twitter_feed_view(request):
    tweets = cache.get('twitter_feed')
    if not tweets:
        tweets = fetch_recent_tweets(username='musharrafaleem')
        cache.set('twitter_feed', tweets, timeout=300)  # cache for 5 minutes
    return render(request, 'integrations/twitter_feed.html', {'tweets': tweets})



