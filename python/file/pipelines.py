import os
import json
from pandas.io.json import json_normalize


class DefaultPipeline(object):

    def __init__(self, analyser=None, storage_strategy=None, geocoder=None):
        '''
            @analyser: instance of an tweetAnalyser
        '''
        self.analyser = analyser()
        self.item = {}
        self.storage_strategy = storage_strategy
        self.geocoder = geocoder
        self.tweet = None

    def analyse(self):
        self.analyser.analyse(self.tweet['text'])
        if self.analyser.sentiment < 0:
            self.item["sentiment"] = "negatif"
        elif self.analyser.sentiment == 0:
            self.item["sentiment"] = "neutre"
        else:
            self.item["sentiment"] = "positif"

    def fetchTweetAttributs(self, tweetAttrs):
        '''Take kwargs representing attributs from the api twitter'''
        tweetAttrs = json.loads(tweetAttrs)
        if self.geocoder:
            for a in tweetAttrs:
                if a == 'user.location':
                    g = self.geocoder(
                        self.tweet['user.location'], key=os.getenv('GEOCODE_TOKEN'))
                    g = g.json
                    try:
                        if g['lat'] or g['lng'] is not None:
                            self.item["user.location"] = {
                                "lat": g['lat'], "lon": g['lng']}
                        else:
                            self.item["user.location"] = {"lat": 0, "lon": 0}
                    except:
                        self.item["user.location"] = {"lat": 0, "lon": 0}
                        pass
                else:
                    self.item[a] = self.tweet[a]

        else:
            for a in tweetAttrs:
                self.item[a] = self.tweet[a]

    def flatten_dict(self, dic):
        return json.loads(json_normalize(
            dic).to_json(orient='records'))[0]

    def ingest(self, tweet):
        '''sending data to the strategy storage'''
        self.tweet = self.flatten_dict(tweet)
        self.analyse()
        self.fetchTweetAttributs(os.getenv('TWEETS_ATTRS'))
        self.storage_strategy.send(self.item)
