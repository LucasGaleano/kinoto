from query import query_users
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
URI = 'http://localhost:9200/_search'

response = requests.get(URI, data=query_users, headers={"content-type":"application/json"})
data = json.loads(response.text)

# Make dataset:
height = [i['doc_count'] for i in data['aggregations']['2']['buckets']]
bars = [i['key'] for i in data['aggregations']['2']['buckets']]
y_pos = np.arange(len(bars))

# Create bars
plt.barh(y_pos, height)

# Create names on the x-axis
plt.yticks(y_pos, bars)


