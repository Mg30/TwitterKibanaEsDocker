
import os
from json.decoder import JSONDecodeError
import json
from pandas.io.json import json_normalize
class DefaultPipeline(object):

    def __init__(self, analyser, tweet, storage_strategy=None, geocoder=None):
        ''' @tweet :  instance of a tweet from the twitterListenner
            @anayser: instance of an tweetAnalyser
        '''
        self.tweet = json.loads(json_normalize(tweet).to_json(orient='records'))[0]
        self.analyser = analyser
        self.item = {}
        self.storage_strategy = storage_strategy
        self.geocoder = geocoder



    def analyse(self):

        self.analyser = self.analyser(self.tweet['text'])
        if self.analyser.sentiment < 0:
            self.item["sentiment"] = "negatif"
        elif self.analyser.sentiment == 0:
            self.item["sentiment"] = "neutre"
        else:
            self.item["sentiment"] = "positif"

    def fetchTweetAttributs(self, tweetAttrs):
        '''Take kwargs representing attributs from the api twitter'''
        if self.geocoder:
            for a in tweetAttrs:
                if a == 'user.location':
                    g = self.geocoder(self.tweet[a], key=os.getenv('GEOCODE_KEY'))
                    try:
                        if g.lat or g.lng is not None:
                            self.item["location"] = {"lat": g.lat, "lon": g.lng}
                        else:
                            self.item["location"] = {"lat": 0, "lon": 0}
                    except JSONDecodeError:
                        pass
                else:
                    self.item[a] = self.tweet[a]

        else:
            for a in tweetAttrs:
                self.item[a] = self.tweet[a]

    def ingest(self):
        '''sending data to the strategy storage'''
        self.analyse()
        self.fetchTweetAttributs(os.getenv('TWEET_ATTRS'))
        self.storage_strategy.send(self.tweet)
