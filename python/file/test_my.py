from pipelines import DefaultPipeline
from tweetAnalyser import TweetBlobAnalyser
import json
import pytest
import geocoder
import os

os.environ['TWITTER_APP_KEY'] = ''
os.environ['TWITTER_APP_SECRET'] = ''
os.environ['TWITTER_KEY'] = ''
os.environ['TWITTER_SECRET'] = ''
os.environ['TRACK_TERMS'] = ''
os.environ['ES_PORT'] = '{"host": "elasticsearch", "port": 9200}'
os.environ['INDEX_NAME'] = 'twitter'
os.environ['INDEX_MAPPING'] = '{"mappings": {"tweet":{"properties": {"sentiment":{"type": "keyword"},"text":{"type": "text"},"location":{"type": "geo_point"},"created_at":{"type": "date"}}}}}'
os.environ['TWEETS_ATTRS'] = '["text", "user.location"]'
os.environ['GEOCODE_TOKEN'] = 'pk.eyJ1IjoicmFuZG9tYWNjZXNzIiwiYSI6ImNqcDh3ZTlpeTA0MXczcHA2cnI5ZGZudnAifQ.aj4dmYSIxfGxciDq30ZBOw'


@pytest.fixture
def tweet():
    with open('tweet.txt') as json_file:
        data = json.load(json_file)
        return data


@pytest.fixture
def geocoder_strat():
    return geocoder.mapbox


def test_analyser(tweet):
    b = TweetBlobAnalyser()
    b.analyse(tweet['text'])
    assert b.sentiment == 0


def test_pipeline_transform(tweet):
    p = DefaultPipeline(analyser=TweetBlobAnalyser)
    p.tweet = tweet
    p.analyse()
    assert p.item["sentiment"] == "neutre"


def test_fetchTweetAttributs(tweet):
    p = DefaultPipeline(analyser=TweetBlobAnalyser)
    t = p.flatten_dict(tweet)
    p.tweet = t
    p.fetchTweetAttributs(os.getenv('TWEETS_ATTRS'))
    assert 'user.location' in p.item.keys()
    assert 'text' in p.item.keys()


def test_flatten_dict(tweet):
    p = DefaultPipeline(analyser=TweetBlobAnalyser)
    t = p.flatten_dict(tweet)
    p.tweet = t
    assert 'user.location' in p.tweet.keys()


def test_fetchTweetAttributs_geo(tweet, geocoder_strat):
    p = DefaultPipeline(analyser=TweetBlobAnalyser, geocoder=geocoder_strat)
    t = p.flatten_dict(tweet)
    p.tweet = t
    p.fetchTweetAttributs(os.getenv('TWEETS_ATTRS'))
    assert 'user.location' in p.item.keys()
