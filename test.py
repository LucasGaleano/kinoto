from elasticsearch import Elasticsearch


es = Elasticsearch(['http://localhost:9200'])

res = es.search(index='ossim-osdepym-2019.04.30', body={'query':{'match_all':{}}})

print(res['hits']['total'])
