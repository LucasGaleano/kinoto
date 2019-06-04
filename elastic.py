from elasticsearch_dsl import connections, Search, A
import json

class Info:


    def crearConexion(self):
        connections.create_connection(hosts=['localhost:9200'],timeout=200)


    def infoWebFilter(self):
        s = Search(index='ossim-osdepym*')
        s = s.query('match',action='block')
        s = s.filter('range', log_date={"gte": 1554087600000,"lte": 1556679599999})
        s.aggs.bucket('users', A('terms', field='user.keyword', size=10, order={ "_count": "desc"}))

        return s.execute().aggregations.users.buckets


    def infoTopApp(self):
        s = Search(index='ossim-osdepym*')
        s = s.query('match_all')
        s = s.filter('range', log_date={"gte": 1554087600000,"lte": 1556679599999})
        s.aggs.bucket('users', A('terms', field='app.keyword', size=5, order={ "_count": "desc"}))

        return s.execute().aggregations.users.buckets


    def infoFlowLogs(self):
        s = Search(index='ossim-osdepym*')
        s = s.query('match_all')
        s = s.filter('range', log_date={"gte": 1554087600000,"lte": 1556679599999})
        s.aggs.bucket('users', A('date_histogram', field='log_date', interval="30m",time_zone="America/Argentina/Buenos_Aires",min_doc_count=1))

        return s.execute().aggregations.users.buckets

    def infoFirewallActions(self):
        s = Search(index='ossim-osdepym*')
        s = s.query('match_all')
        s = s.filter('range', log_date={"gte": 1554087600000,"lte": 1556679599999})
        s.aggs.bucket('actions', A('terms', field='action.keyword', size=10, order={ "_count": "desc"}))

        return s.execute().aggregations.actions.buckets
