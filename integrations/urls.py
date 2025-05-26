from django.urls import path
from . import views

urlpatterns = [
    path('twitter/', views.twitter_feed_view, name='twitter-feed'),
    path('facebook/', views.facebook_feed_view, name='facebook_feed'),

]
