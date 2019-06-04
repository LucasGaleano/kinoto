from elasticsearch_dsl import connections, Search, A
import json

class Info:


    def crearConexion(self):
        connections.create_connection(hosts=['localhost:9200'],timeout=200)


    def infoWebFilter(self):
        s = Search(index='ossim-osdepym*')
        s = s.query('match',action='block')
        s = s.filter('range', log_date={"gte": 1554087600000,"lte": 1556679599999})
        s.aggs.bucket('users', A('significant_terms', field='user.keyword', size=10))

        webFilter  = s.execute().aggregations.users.buckets
        return webFilter

    def infoTopApp(self):
        s = Search(index='ossim-osdepym*')
        s = s.query('match_all')
        s = s.filter('range', log_date={"gte": 1554087600000,"lte": 1556679599999})
        s.aggs.bucket('users', A('significant_terms', field='app.keyword', size=5))

        topApp  = s.execute().aggregations.users.buckets
        return topApp
