from pipelines import DefaultPipeline
from tweetAnalyser import TweetBlobAnalyser
import json
import pytest
import geocoder


@pytest.fixture
def tweet():
    with open('tweet.txt') as json_file:
        data = json.load(json_file)
        return data


@pytest.fixture
def geocoder_strat():
    return geocoder.mapbox


def test_analyser(tweet):
    b = TweetBlobAnalyser(tweet['text'])
    assert b.analyse() == 0


def test_pipeline_transform(tweet):
    p = DefaultPipeline(analyser=TweetBlobAnalyser)
    p.tweet = tweet
    p.analyse()
    assert p.item["sentiment"] == "neutre"


def test_fetchTweetAttributs(tweet):
    p = DefaultPipeline(analyser=TweetBlobAnalyser)
    p.tweet = tweet
    p.fetchTweetAttributs(['created_at', 'text'])
    assert 'created_at' in p.item.keys()
    assert 'text' in p.item.keys()


def test_flatten_dict(tweet):
    p = DefaultPipeline()
    t = p.flatten_dict(tweet)
    p.tweet = t
    assert 'user.location' in p.tweet.keys()

def test_fetchTweetAttributs_geo(tweet, geocoder_strat):
    p = DefaultPipeline(analyser=TweetBlobAnalyser, geocoder=geocoder_strat)
    t = p.flatten_dict(tweet)
    p.tweet = t
    p.fetchTweetAttributs(['user.location'])
    assert 'location' in p.item.keys()
