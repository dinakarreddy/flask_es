import os
import json
from elasticsearch_dsl.connections import connections

ES_HOST = os.environ['ES_HOST']

connections.create_connection(hosts=[ES_HOST])
ES_CLIENT = connections.get_connection()
INIT_ES_INDEX = json.loads(os.environ.get('INIT_ES_INDEX', 'false'))
