import Settings
import time
import tweepy
import geocoder
import json
import re
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
from ElasticApi import Elastic


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
        try:
            g = geocoder.mapquest(status.user.location, key=Settings.api_key)
            if g.lat or g.lng is not None:
                item["location"] = {"lat": g.lat, "lon": g.lng}
            else:
                item["location"] = {"lat": 0, "lon": 0}

        except json.decoder.JSONDecodeError:
            pass
        es.document_add(Settings.INDEX_NAME,Settings.DOC_TYPE,item)
        #else:
            #return

    def on_error(self, status_code):
        """fonction qui gère les erreurs issus de l'api twitter"""
        if status_code == 420:
            print("fin")
            return False

#***********************DEBUT DU PROGRAMME****************************************************************************************

mapping = {"mappings": {"tweet":{"properties": {"sentiment":{"type": "keyword"},"text":{"type": "text"},"location":{"type": "geo_point"},"time":{"type": "date"}}}}}
connected = False
es = Elastic(Settings.ES_HOST)

#test pour savoir si elastic est prêt à recevoir des données
while not connected:
    
        if not es.ping():
            print("Elasticsearch est en cours de démarrage...")
            time.sleep(5)
        else:
            print("elastic est prêt")
            connected = True
            time.sleep(5)

#Création de l'index pour alimenter le flux twitter
es.create_index(Settings.INDEX_NAME,mapping=mapping)
            
#Authentification pour acceder a l'api twitter
auth = tweepy.OAuthHandler(Settings.TWITTER_APP_KEY, Settings.TWITTER_APP_SECRET)
auth.set_access_token(Settings.TWITTER_KEY, Settings.TWITTER_SECRET)
api = tweepy.API(auth) #creation d'un objet API contenant les informations de connexion
stream_listener = StreamListener() # instance de la classe streamlistener
stream = tweepy.Stream(auth=api.auth, listener= stream_listener) # création de stream twitter avec api et la class pour gérer les tweets
stream.filter(track=[Settings.TRACK_TERMS])


