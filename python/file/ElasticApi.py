from elasticsearch import Elasticsearch

class Elastic:
    """Classe qui permet de communiquer avec api elasticsearch"""


    def __init__(self, port):
        self.es = Elasticsearch(hosts=[port])

    def create_index(self,index_name,mapping=None):
        """Functionality to create index."""
        resp = self.es.indices.create(index=index_name,body=mapping)
        print(resp)


    def document_add(self, index_name,doc_type, doc, doc_id=None):
        """Funtion to add a document by providing index_name,
    document type, document contents as doc and document id."""
        resp = self.es.index(index=index_name, doc_type= doc_type, body=doc, id=doc_id)
        print(resp)


    def document_view(self,index_name,doc_type, doc_id):
        """Function to view document."""
        resp = self.es.get(index=index_name, doc_type=doc_type, id=doc_id)
        document = resp["_source"]
        print(document)


    def document_update(self, index_name,doc_type, doc_id, doc=None, new=None):
        """Function to edit a document either updating existing fields or adding a new field."""
        if doc:
            resp = self.es.index(index=index_name, doc_type=doc_type,
                        id=doc_id, body=doc)
            print(resp)
        else:
            resp = self.es.update(index=index_name, doc_type=doc_type,
                         id=doc_id, body={"doc": new})


    def document_delete(self,index_name,doc_type, doc_id):
        """Function to delete a specific document."""
        resp = self.es.delete(index=index_name, doc_type=self.doc_type, id=doc_id)
        print(resp)


    def delete_index(self,index_name):
        """Delete an index by specifying the index name"""
        resp = self.es.indices.delete(index=index_name)
        print(resp)

    def restore(rep_name,snap_name,body=None):
        snap = elasticsearch.client.SnapshotClient(self.es)
        resp = snap.restore(repository=rep_name,snapshot=snap_name,wait_for_completion=True)
        print(resp)
        
    def ping(self):
        return self.es.ping()
