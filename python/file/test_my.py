from pipelines import DefaultPipeline
from tweetAnalyser import TweetBlobAnalyser

import pytest


class TweetTest(object):
    def __init__(self):
        self.text = "test"
        self.fake = "fake"


@pytest.fixture
def tweet():
    return TweetTest()


def test_analyser(tweet):
    b = TweetBlobAnalyser(tweet.text)
    assert b.analyse() == 0


def test_pipeline_transform(tweet):
    p = DefaultPipeline(TweetBlobAnalyser, tweet)
    p.analyse()
    assert p.item["sentiment"] == "neutre"


def test_fetchTweetAttributs(tweet):
    p = DefaultPipeline(TweetBlobAnalyser, tweet)
    p.fetchTweetAttributs('fake','text')
    assert 'fake' in p.item.keys()
    assert 'text' in p.item.keys()
