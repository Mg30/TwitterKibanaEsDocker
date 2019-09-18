import tweepy

class StreamListener(tweepy.StreamListener):
        """ Classe qui herite de streamlistener qui va gérer le flux de données issus de twitter"""

        def __init__(self, pipeline):
            self.pipeline = pipeline

        def on_status(self, status):
            """fonction qu permet d'effectuer une action pour chaque tweet arrivant de l'api"""

            if hasattr(status, 'retweeted_status'):  # excluding retweet
                return
            self.pipeline.ingest(status._json)

        def on_error(self, status_code):
            """fonction qui gère les erreurs issus de l'api twitter"""
            if status_code == 420:
                print("fin")
                return False
