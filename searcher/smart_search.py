from elasticsearch import Elasticsearch
from bson.objectid import ObjectId
from db.db import posts
from modules.decorators import default_decorator


@default_decorator('error in elastic find docs')
def find_n_docs(elastic_host, index_name, count, text):
    es = Elasticsearch(elastic_host)
    res = es.search(index=index_name, query={"match": {"text": text}})
    data = res['hits']['hits']
    return data[:count]


@default_decorator('error in finding mongo docs')
def get_docs_from_db(mongo_collection, elastic_data):
    id_list = []
    for i in elastic_data:
        id_list.append(ObjectId(i['_id']))
    data = mongo_collection.find({"_id": {"$in": id_list}}).sort('created_date')
    data = list(data)
    for object in data:
        object['_id'] = str(object['_id'])
    return data


if __name__ == '__main__':
    data = find_n_docs('http://localhost:9200', 'posts', 20, 'тестовый текст')
    print(get_docs_from_db(posts, data))
