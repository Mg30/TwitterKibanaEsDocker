from textblob import TextBlob
from textblob_fr import PatternAnalyzer, PatternTagger


class TweetBlobAnalyser(object):

    def __init__(self, tweet):
        self.blob = TextBlob(tweet,pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        self.sentiment = self.analyse()

    def analyse(self):
        return self.blob.sentiment[0]
