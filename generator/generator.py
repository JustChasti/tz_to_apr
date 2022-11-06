from generator.mongo_import import mongoimport
from elastic_generator import generate_elastic_endex
from config import elastic_host, elastic_index
from modules.decorators import default_decorator


@default_decorator('generator error')
def generate(input_file, collection):
    mongoimport(input_file, collection)
    generate_elastic_endex(elastic_host, elastic_index, collection)
    return {'message': 'data in mongo and elastic generated'}
