from textblob import TextBlob
from textblob_fr import PatternAnalyzer, PatternTagger


class TweetBlobAnalyser(object):
    '''Class analyse a string using blob librairie
    constructor take @tweet : string
    '''

    def __init__(self):
        self.sentiment = None

    def analyse(self,tweet):
        blob = TextBlob(tweet, pos_tagger=PatternTagger(),
                        analyzer=PatternAnalyzer())
        self.sentiment = blob.sentiment[0]
