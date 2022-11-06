from elasticsearch import Elasticsearch
from db.db import posts


def generate_elastic_endex(elastic_host, index_name, mongo_document):
    es = Elasticsearch(elastic_host)
    elements = mongo_document.find({})
    for i in elements:
        es.index(index=index_name, id=str(i['_id']), document={'text': i['text']})


def get_examle_doc(elastic_host, index_name, id):
    es = Elasticsearch(elastic_host)
    res = es.get(index=index_name, id=id)
    print(res['_source'])


if __name__ == '__main__':
    pass
    # generate_elastic_endex('http://localhost:9200', 'posts', posts)
    # get_examle_doc('http://localhost:9200', 'posts', '63652edbd5c9bad3c3927e8e')
