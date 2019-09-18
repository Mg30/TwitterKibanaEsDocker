import Settings # fichier de confguration
import time # librairie de base utilisé pour faire attendre le script
import tweepy#libraiire qui sert à communiuqer avec api twitter
import geocoder# librairie qui sert à communiuqer avec api de geocodage
import json# module qui permet de traiter les fichiers json
from textblob import TextBlob # module qui permet de réaliser l'analyse de sentiment
from textblob_fr import PatternTagger, PatternAnalyzer
from ElasticApi import Elastic # import de la classe personnalisé permettant de communquer avec ES




#***********************DEBUT DU PROGRAMME****************************************************************************************

mapping = {"mappings": {"tweet":{"properties": {"sentiment":{"type": "keyword"},"text":{"type": "text"},"location":{"type": "geo_point"},"time":{"type": "date"}}}}} # MAPPING DE L INDEX ES
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
try:
    es.delete_index(Settings.INDEX_NAME)
except:
    pass
try:
    es.create_index(Settings.INDEX_NAME,mapping=mapping)
except:
    pass
            
#Authentification pour acceder a l'api twitter
auth = tweepy.OAuthHandler(Settings.TWITTER_APP_KEY, Settings.TWITTER_APP_SECRET)
auth.set_access_token(Settings.TWITTER_KEY, Settings.TWITTER_SECRET)
api = tweepy.API(auth) #creation d'un objet API contenant les informations de connexion
stream_listener = StreamListener() # instance de la classe streamlistener definie en haut
stream = tweepy.Stream(auth=api.auth, listener= stream_listener) # création de stream twitter avec api et la class pour gérer les tweets
stream.filter(track=[Settings.TRACK_TERMS]) # début du stream en utilisant le terme défini dans Settings


