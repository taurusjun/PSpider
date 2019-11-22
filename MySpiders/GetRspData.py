#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from prettytable import PrettyTable
import requests
import json

from DBOps import DBOperator

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
                    # {
                    #     "dCityCode":"TYO",
                    #     "aCityCode":"SFO",
                    #     "dDate":"2019-12-13"
                    # }
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

version='20191121'
dCity='TYO'
aCity='SFO'
dDate='2019-12-13'

searchSegmentList = request_payload_batch_search['variables']['request']['searchInfo']['searchSegmentList']
searchSegmentList.append({'dCityCode': dCity,
                          'aCityCode': aCity,
                          'dDate':dDate});

s = requests.session()
response = s.post(url_batch_search, data=json.dumps(request_payload_batch_search), headers=headers_batch_search).text

print(response)

flightSearchRslt = json.loads(response).get('data').get('intlFlightListSearch')
if flightSearchRslt.get('ResponseStatus').get('Ack') == 'Success' and \
                flightSearchRslt.get('responseHead').get('errorCode')=='0':
    DBOperator.updateOrCreateRsponse(departureCityCode=dCity,
                                     arrivalCityCode=aCity,
                                     scheduleDate=dDate,
                                     version=version,
                                     responseDate=response)

