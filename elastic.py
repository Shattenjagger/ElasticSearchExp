import json
import requests

index_name = 'test_index'
elastic_url = 'http://%s:%s/' % ('127.0.0.1', '9201')
elastic_index_url = '%s%s/' % (elastic_url, index_name)

def list_indices():
    r = requests.get(elastic_url + '_cat/indices?v')
    print r.status_code
    print r.text


def create_index():
    r = requests.put(elastic_index_url)
    print r.status_code
    print r.text

def get_index():
    r = requests.get(elastic_index_url)
    print r.status_code
    print r.text

# list_indices()
# create_index()
# list_indices()
get_index()

# def create_document(data, namespace):
#     url = "%s%s/%s/" % (elastic_index_url, namespace, data['id'])
#     r = requests.put(url, data=json.dumps(data))
#     print r.status_code
#     print r.text
#
#
# for i in range(0, 10):
#     person = {
#         "id": i,
#         "name": "Person %s" % i
#     }
#     create_document(person, 'persons')
