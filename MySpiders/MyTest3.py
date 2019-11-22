#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from prettytable import PrettyTable
import requests
import json

from DBOps import DBOperator
from DBOps.db.models import schedule

url_batch_search = 'https://www.trip.com/flightapi/graphql/intlFlightListSearch'
headers_batch_search = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'Content-Type': 'application/json',
    'Cookie':'ibulocale=en_xx;_abtest_userid=639eb3ed-e1a6-4541-a29c-74a2d23e4437;ibulanguage=EN;;'
}

request_payload_batch_search={
    "operationName":"intlFlightListSearch",
    "variables":{
        "request":{
            "searchNo":"1",
            "mode":0,
            # "productKeyInfo":null,
            "criteriaToken":"",
            "searchInfo":{
                "tripType":"OW",
                "cabinClass":"YS",
                "travelerNum":{
                    "adult":1,
                    "child":1,
                    "infant":1
                },
                "searchSegmentList":[
                    {
                        "dCityCode":"TYO",
                        "aCityCode":"SFO",
                        "dDate":"2019-12-13"
                    },
                    {
                        "dCityCode": "TYO",
                        "aCityCode": "SFO",
                        "dDate": "2019-12-14"
                    }
                ]
            }
        }
    },
    "extensions":{
        "persistedQuery":{
            "version":1,
            "sha256Hash":"827bb24e09e3c29d0a6474ea5787069d21e13a87a24f9a377db3b542539515c8"
        }
    }
}

proxies = {
  "http": "localhost:8888",
  "https": "localhost:8888",
}

s = requests.session()
# c = requests.cookies.RequestsCookieJar()
# c.set('_abtest_userid', '0ca24f7e-689e-4db4-b036-73b7f428e7a1;', path='/', domain='.trip.com')
# c.set('ibulanguage', 'en', path='/', domain='.trip.com')
# c.set('ibulocale', 'en_xx', path='/', domain='.trip.com')
# s.cookies.update(c)
# response = s.post(url_batch_search, data=json.dumps(request_payload_batch_search), headers=headers_batch_search, proxies=proxies, verify='/Users/wangjun/Downloads/charles-ssl-proxying-certificate.pem').text
response = s.post(url_batch_search, data=json.dumps(request_payload_batch_search), headers=headers_batch_search).text

# response = requests.post(url_batch_search, data=json.dumps(request_payload_batch_search), headers=headers_batch_search, cookies=cookies,proxies=proxies, verify='/Users/wangjun/Downloads/charles-ssl-proxying-certificate.pem').text
# response = requests.post(url_batch_search, data=json.dumps(request_payload_batch_search), headers=headers_batch_search).text
# response = requests.post(url_batch_search, data=request_payload_batch_search, headers=headers_batch_search).text

# response = requests.get('http://www.baidu.com',headers=headers_batch_search,cookies=cookies,proxies=proxies)
print(response)

# flightSearchRslt = json.loads(response).get('data').get('intlFlightListSearch')
# if flightSearchRslt.get('ResponseStatus').get('Ack') == 'Success' and \
#                 flightSearchRslt.get('responseHead').get('errorCode')=='0':
#     productInfoList = flightSearchRslt.get('productInfoList')
#
#     idx=0
#
#     version = '20191121'
#     bizId = '20191213TYOSFO'
#
#     myschedule = DBOperator.updateOrCreateSchedule('TYO', 'SFO', '2019-12-13', bizId, version, 'running')
#     # myschedule= schedule(departureCityCode='TYO',
#     #                      arrivalCityCode='SFO',
#     #                      scheduleDate='2019-12-10',
#     #                      bizId=bizId)
#     # myschedule.trips=[]
#
#     # scheduleSubId = str(myschedule.id)+"-1"
#     # product = productInfoList[0]
#     # DBOperator.saveSingleFlightProduct(product, myschedule.id)
#     # mTrip = DBOperator.createSingleFlightProduct(product, myschedule.id, scheduleSubId)
#     # print "aa"
#     for product in productInfoList:
#         idx=idx+1
#         scheduleSubId = bizId+"-"+str(idx)
#         DBOperator.saveSingleFlightProduct(product, myschedule.id, scheduleSubId, version)
#         # mTrip = DBOperator.createSingleFlightProduct(product, scheduleSubId)
#         # myschedule.trips.append(mTrip)
#
# DBOperator.updateScheduleStatus(myschedule,'finished')
# # import redis
# # import pickle
# # r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# # pickled_object = pickle.dumps(myschedule)
# # r.set('20191209', pickled_object)
