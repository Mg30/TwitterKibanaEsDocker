import os
import tweepy
from pipelines import DefaultPipeline
from geocoder import mapbox
from adaptaters import ElasticSearchAdaptater
from tweetAnalyser import TweetBlobAnalyser
from twitterListener import CustomStreamListener
import json

mapping = os.getenv('INDEX_MAPPING')
mapping = json.loads(mapping)


es = ElasticSearchAdaptater(port=json.loads(os.getenv('ES_PORT')),
                            index_name=os.getenv('INDEX_NAME'),
                            mapping=mapping)
es.initialize()

pipeline = DefaultPipeline(geocoder=mapbox,
                           storage_strategy=es,
                           analyser=TweetBlobAnalyser
                           )


# Initializing twitter auth
auth = tweepy.OAuthHandler(os.getenv('TWITTER_APP_KEY'),
                           os.getenv('TWITTER_APP_SECRET'))

auth.set_access_token(os.getenv('TWITTER_KEY'),
                      os.getenv('TWITTER_SECRET'))
api = tweepy.API(auth)

# Initializing the stream
stream_listener = CustomStreamListener(pipeline=pipeline)
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=json.loads(os.getenv('TRACK_TERMS')))
