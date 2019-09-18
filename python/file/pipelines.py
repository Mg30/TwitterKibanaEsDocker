

class DefaultPipeline(object):

    def __init__(self, analyser, tweet):
        ''' @tweet :  instance of a tweet from the twitterListenner
            @anayser: instance of an tweetAnalyser
        '''
        self.tweet = tweet
        self.analyser = analyser
        self.item = {}

    def analyse(self):

        self.analyser = self.analyser('test')
        if self.analyser.sentiment < 0:
            self.item["sentiment"] = "negatif"
        elif self.analyser.sentiment == 0 :
            self.item["sentiment"] = "neutre"
        else:
            self.item["sentiment"] = "positif"

    
    def fetchTweetAttributs(self, *args):
        '''Take kwargs representing attributs from the api twitter'''
        for a in args:
            self.item[a] = getattr(self.tweet, a)

    
    def ingest(self):
        pass
