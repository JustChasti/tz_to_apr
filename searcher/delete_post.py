from elasticsearch import Elasticsearch
from bson.objectid import ObjectId
from loguru import logger
from modules.decorators import default_decorator


@default_decorator('error in deletion from elastic or mongo')
def deletion(elastic_host, index_name, collection, id):
    from_elastic(elastic_host, index_name, id)
    from_mongo(collection, id)
    return {'message': f'deletion element {id} succes'}


def from_elastic(elastic_host, index_name, id):
    es = Elasticsearch(elastic_host)
    res = es.delete(index=index_name, id=id)
    logger.info(res)


def from_mongo(collection, id):
    res = collection.delete_one({"_id": ObjectId(id)})
    logger.info(res)
