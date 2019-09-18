import tweepy
f
from Settings import ES_HOST,api_key,TRACK_TERMS,INDEX_NAME,DOC_TYPE
import geocoder
import json
import re

 
class StreamListener(tweepy.StreamListener):
    """ Classe qui herite de streamlistener qui va gérer le flux de données issus de twitter"""

    def on_status(self, status):
        """fonction qu permet d'effectuer une action pour chaque tweet arrivant de l'api"""

        if hasattr(status,'retweeted_status'): # excluding retweet
            return

# on ajoute au dict le texte du tweet
        item["text"] = status.text
# on ajoute sa date de cr"ation
        item["time"] = status.created_at
        #bloc qui permet de récuprer la géolocation
        try:
            g = geocoder.mapquest(status.user.location, key=Settings.api_key)
            if g.lat or g.lng is not None:
                item["location"] = {"lat": g.lat, "lon": g.lng}
            else:
                item["location"] = {"lat": 0, "lon": 0}

        except json.decoder.JSONDecodeError:
            pass
        #envoie du tweet à l'indice ES
        es.document_add(Settings.INDEX_NAME,Settings.DOC_TYPE,item)
        #else:
            #return

    def on_error(self, status_code):
        """fonction qui gère les erreurs issus de l'api twitter"""
        if status_code == 420:
            print("fin")
            return False
