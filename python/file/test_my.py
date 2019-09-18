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
    p = DefaultPipeline(TweetBlobAnalyser, tweet)
    p.analyse()
    assert p.item["sentiment"] == "neutre"


def test_fetchTweetAttributs(tweet):
    p = DefaultPipeline(TweetBlobAnalyser, tweet)
    p.fetchTweetAttributs(['created_at','text'])
    assert 'created_at' in p.item.keys()
    assert 'text' in p.item.keys()

def test_fetchTweetAttributs_geo(tweet,geocoder_strat):
    p = DefaultPipeline(TweetBlobAnalyser, tweet, geocoder_strat)
    p.fetchTweetAttributs(['user.location'])
    assert 'location' in p.item.keys()