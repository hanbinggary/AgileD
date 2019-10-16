from elasticsearch import Elasticsearch


class ESUtils:
    def __init__(self, index, **es_config):
        self.index = index
        self.address = es_config.setdefault("address", "127.0.0.1")
        self.username = es_config.setdefault("username", "")
        self.password = es_config.setdefault("password", "")

    def __enter__(self):
        self.es = Elasticsearch([self.address])
        return self

    def search_data(self, query_body):
        return self.es.search(index=self.index, body=query_body)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
