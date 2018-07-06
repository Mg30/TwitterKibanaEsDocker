import tweepy
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from Settings import ES_HOST,api_key,TRACK_TERMS,INDEX_NAME,DOC_TYPE
import geocoder
import json
import re

 
class StreamListener(tweepy.StreamListener):
    """ Classe qui va gérer le flux de données issus de twitter"""

    def on_status(self, status):
        """fonction qu permet d'effectuer une action pour chaque tweet arrivant de l'api"""
        if hasattr(status,'retweeted_status'):
            return
        #if regex.search(status.text.lower()):
        blob = TextBlob(status.text,pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        sent = blob.sentiment
        item = dict()
        if sent[0] < 0:
            item["sentiment"] = "negatif"
        elif sent[0] == 0:
            item["sentiment"] = "neutre"
        else:
            item["sentiment"] = "positif"

        item["text"] = status.text

        item["time"] = status.created_at
        m = regex.search(status.text.lower())
        if m:
            item["score"] = m.group(0)
        try:
            g = geocoder.mapquest(status.user.location, key=api_key)
            if g.lat or g.lng is not None:
                item["location"] = {"lat": g.lat, "lon": g.lng}
            else:
                item["location"] = {"lat": 0, "lon": 0}

        except json.decoder.JSONDecodeError:
            pass
        print(item)
        es.document_add(INDEX_NAME,DOC_TYPE,item)
        #else:
            #return

    def on_error(self, status_code):
        """fonction qui gère les erreurs issus de l'api twitter"""
        if status_code == 420:
            print("fin")
            return False
