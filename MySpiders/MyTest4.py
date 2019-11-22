#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import json

import requests

from DBOps import DBOperator

url_batch_search = 'https://www.trip.com/flightapi/graphql/poiSearch'
headers_batch_search = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Content-Type": "application/json",  # 声明文本类型为 json 格式
}
request_payload_batch_search={
    "operationName": "poiSearch",
    "variables":
        {
            "key": "T",
            "mode": 0
        },
    "extensions":
        {
            "persistedQuery":
                {
                    "version": 1,
                    "sha256Hash": "bb3f6188163edbdef49813b1f4552a01fde15ab6daddaca4b0494125a5d7cef8"
                }
        }
}

proxies = {
  "http": "localhost:8888",
  "https": "localhost:8888",
}

response = requests.post(url_batch_search,
                         data=json.dumps(request_payload_batch_search),
                         headers=headers_batch_search,
                         # proxies=proxies,
                         # verify='/Users/wangjun/Downloads/charles-ssl-proxying-certificate.pem'
                         ).text
# response = requests.post(url_batch_search, data=request_payload_batch_search, headers=headers_batch_search).text
# response = requests.get('https://www.trip.com', headers=headers_batch_search,proxies=proxies, verify='/Users/wangjun/Downloads/charles-ssl-proxying-certificate.pem').text
poiSearchRslt = json.loads(response).get('data').get('poiSearch')
if poiSearchRslt.get('ResponseStatus').get('Ack') == 'Success':
    poiInfoRsltList = poiSearchRslt.get('results')
    size = len(poiInfoRsltList)
    # DBOperator.saveAsPOIInfo(poiInfoRsltList[0])
    for poiInfo in poiInfoRsltList:
        DBOperator.saveAsPOIInfo(poiInfo)


print(response)

