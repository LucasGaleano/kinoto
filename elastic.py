from elasticsearch_dsl import connections, Search, A
import json
import numpy as np
import matplotlib.pyplot as plt

connections.create_connection(hosts=['localhost:9200'],timeout=200)

s = Search(index='ossim-osdepym*')
s = s.query('match',action='block')
s = s.filter('range', log_date={"gte": 1554087600000,"lte": 1556679599999})
s.aggs.bucket('users', A('significant_terms', field='user.keyword', size=20))


#print(json.dumps(s.to_dict(), indent=1))
response  = s.execute().aggregations.users.buckets

# Make dataset:
height = [x['doc_count'] for x in response]
bars = [x['key'] for x in response]
y_pos = np.arange(len(bars))

# Create bars
plt.barh(y_pos, height)

# Create names on the x-axis
plt.yticks(y_pos, bars)

# Show graphic
plt.show()
