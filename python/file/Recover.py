#test pour savoir si l'instance Elastic est disponible
import time
from elasticsearch import Elasticsearch
from elasticsearch.client import SnapshotClient
connected = False
ES_HOST = {"host": "elasticsearch", "port": 9200}
es = Elasticsearch(hosts=[ES_HOST])
registerBody= {"type": "fs", "settings": {"location": "scrapy-2018-06-2018-06"}}
while not connected:
    
        if not es.ping():
            print("Elasticsearch est en cours de démarrage...")
            time.sleep(5)
        else:
            print("elastic est prêt")
            connected = True
            time.sleep(5)
            
snap = SnapshotClient(es)
rep = snap.create_repository(repository="scrapy-2018-06-2018-06",body=registerBody)             
resp = snap.restore(repository="scrapy-2018-06-2018-06",snapshot="juin18",wait_for_completion=True)
print(resp)






        

    

