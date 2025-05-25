from django.urls import path
from . import views

urlpatterns = [
    path('twitter/', views.twitter_feed_view, name='twitter-feed'),
]
