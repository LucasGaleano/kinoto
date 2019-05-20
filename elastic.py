from elasticsearch_dsl import connections, Search, A
import json


connections.create_connection(hosts=['localhost:9200'],timeout=200)

s = Search(index='ossim-osdepym*')
s = s.query('match',action='block')
s = s.filter('range', log_date={"gte": 1554087600000,"lte": 1556679599999})
s.aggs.bucket('users', A('significant_terms', field='user.keyword', size=20))


#print(json.dumps(s.to_dict(), indent=1))
response  = s.execute().aggregations.users.buckets
