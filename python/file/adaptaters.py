from elasticsearch import Elasticsearch
from abc import ABC, abstractmethod

class StorageAdaptater(ABC):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def send(self):
        pass


class ElasticSearchAdaptater(StorageAdaptater):
    '''Adaptater for the ElasticStrategy
    '''

    def __init__(self, **kwargs):
        if not 'port' in kwargs.keys():
            raise Exception('port number needed')
        elif not 'mapping' in kwargs.keys():
            raise Exception('mapping needed')
        elif not 'index_name' in kwargs.keys():
            raise Exception('index_name  needed')
        else:
            self.kwargs = kwargs
            self.es = Elasticsearch(hosts=[kwargs['port']])

    def initialize(self):
        ''' initialization of a working index in es client'''
        import time
        connected = False

        while not connected:
            if not self.es.ping():
                print("Elasticsearch est en cours de démarrage...")
                time.sleep(2)
            else:
                connected = True
        try:
            self.es.indices.create(
                index=self.kwargs['index_name'], body=self.kwargs['mapping'])
        except:
            pass

    def send(self, data):
        '''Wrapper method to add one document to es index'''
        resp = self.es.index(index=self.kwargs['index_name'],
                      doc_type='tweet', body=data)
        print(resp)
