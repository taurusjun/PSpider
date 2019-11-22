#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from prettytable import PrettyTable
import requests
import json

from DBOps import DBOperator
from DBOps.db.models import *



response = DBOperator.oneResponseObj()
jsonData = response.respData

flightSearchRslt = json.loads(jsonData).get('data').get('intlFlightListSearch')

version = '20191121'
bizId = '20191213TYOSFO'
myschedule = DBOperator.updateOrCreateSchedule('TYO', 'SFO', '2019-12-13', bizId, version, 'running')

if flightSearchRslt.get('ResponseStatus').get('Ack') == 'Success' and \
                flightSearchRslt.get('responseHead').get('errorCode')=='0':


    productInfoList = flightSearchRslt.get('productInfoList')

    idx=0

    for product in productInfoList:
        idx=idx+1
        scheduleSubId = bizId+"-"+str(idx)
        DBOperator.saveSingleFlightProduct(product, myschedule.id, scheduleSubId, version)

    DBOperator.updateScheduleStatus(myschedule,'finished')
else:
    DBOperator.updateScheduleStatus(myschedule, 'Error','Not a success response')
