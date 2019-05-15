import json

query_users = json.dumps({
  "aggs": {
    "2": {
      "significant_terms": {
        "field": "user.keyword",
        "size": 20
      }
    }
  },
  "size": 0,
  "_source": {
    "excludes": []
  },
  "stored_fields": [
    "*"
  ],
  "script_fields": {},
  "docvalue_fields": [

    {
      "field": "log_date",
      "format": "date_time"
    }
  ],
  "query": {
    "bool": {
      "must": [
        {
          "match_all": {}
        },
        {
          "match_all": {}
        },
        {
          "match_phrase": {
            "action.keyword": {
              "query": "block"
            }
          }
        },
        {
          "range": {
            "log_date": {
              "gte": 1554087600000,
              "lte": 1556679599999,
              "format": "epoch_millis"
            }
          }
        }
      ],
      "filter": [],
      "should": [],
      "must_not": [
        {
          "match_phrase": {
            "user.keyword": {
              "query": "N/A"
            }
          }
        }
      ]
    }
  }
})
