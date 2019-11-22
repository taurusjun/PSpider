#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os

from django.db import transaction
from django.db.models import Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DBOps.settings")
import django

django.setup()

# Import your models for use in your script
from DBOps.db.models import *

def showInfos():
    for u in POIInfo.objects.all():
        print("ID: " + str(u.ID) + "\tInfo: " + str(u))

def saveAsPOIInfo(poiInfoDict):

    id=saveSinglePoiInfo(poiInfoDict,0)

    cInfoList = poiInfoDict['childResults']
    if cInfoList is None:
        return

    # 子结果
    for cInfo in cInfoList:
        saveSinglePoiInfo(cInfo,id)

def saveSinglePoiInfo(singlePoiInfoDict, pId):
    pPoiId = singlePoiInfoDict['poiId']
    if POIInfo.objects.filter(poiId=pPoiId).exists():
        print "Already exists! poiId = " + str(pPoiId)
        return

    poiInfo = POIInfo(
        poiId=singlePoiInfoDict['poiId'],
        cityCode=singlePoiInfoDict['cityCode'],
        cityEName = singlePoiInfoDict['cityEName'],
        name=singlePoiInfoDict['name'],
        countryName=singlePoiInfoDict['countryName'],
        countryCode=singlePoiInfoDict['countryCode'],
        distance=singlePoiInfoDict['distance'],
        isDomestic=singlePoiInfoDict['isDomestic'],
        isCanSelect=singlePoiInfoDict['isCanSelect'],
        airportCode=singlePoiInfoDict['airportCode'],
        provinceName=singlePoiInfoDict['provinceName'],
        provinceCode=singlePoiInfoDict['provinceCode'],
        mapWord=singlePoiInfoDict['mapWord'],
        dataType=singlePoiInfoDict['dataType'],
        airportShortName=singlePoiInfoDict['airportShortName'],
        virtualRegionCode=singlePoiInfoDict['virtualRegionCode'],
        timeZone=singlePoiInfoDict['timeZone'],
        poiParentId=pId
    )
    poiInfo.save()
    print "Save success id = " + str(poiInfo.ID)
    return poiInfo.ID

def oneResponseObj():
    return Response.objects.get(id=1)

def updateOrCreateRsponse(departureCityCode, arrivalCityCode, scheduleDate, version, responseDate):
    newResp,created= Response.objects.update_or_create(
        departureCityCode=departureCityCode,
        arrivalCityCode=arrivalCityCode,
        scheduleDate=scheduleDate,
        defaults={'version':version, 'respData':responseDate}
    )

def updateScheduleStatus(schedule,status, reason):
    schedule.status=status
    schedule.errorReason=reason
    schedule.save()

def updateOrCreateSchedule(departureCityCode, arrivalCityCode, scheduleDate, bizId, version, status):
    newschedule,created= schedule.objects.update_or_create(
        departureCityCode=departureCityCode,
        arrivalCityCode=arrivalCityCode,
        scheduleDate=scheduleDate,
        bizId=bizId,
        version=version,
        defaults={'status':status}
    )

    return newschedule;

@transaction.atomic
def saveSingleFlightProduct(productJson,scheduleDateRef, scheduleSubId, version):
    cityStopInfoStr=""
    cityStopInfoList = productJson.get('cityStopInfoList')
    if cityStopInfoList is not None:
        cityStopInfoStr= "|".join([cityStopInfo.get('code') for cityStopInfo in cityStopInfoList])

    newtrip = trip(departureCityCode=productJson.get('dCityInfo').get('code'),
                   arrivalCityCode=productJson.get('aCityInfo').get('code'),
                   departureTime=productJson.get('dDateTime'),
                   arrivalTime=productJson.get('aDateTime'),
                   cityStopList=cityStopInfoStr,
                   currency=productJson.get('currency'),
                   isShortestDrt=productJson.get('isShortestDrt'),
                   isLowestPrice=productJson.get('isLowestPrice'),
                   durationMin=productJson.get('durationMin'),
                   arrivalDays=productJson.get('arrivalDays'),
                   scheduleRefId=scheduleDateRef,
                   scheduleSubId=scheduleSubId,
                   version=version
                   )
    newtrip.save()
    # ------------ flight -------------------
    flightInfoList = productJson.get('flightInfoList')
    if flightInfoList is not None:
        for flightInfo in flightInfoList:
            craftInfo = flightInfo.get('craftInfo')
            if craftInfo is not None:
                craftName = craftInfo.get('name')
                craftObj = None
                if craftName is not None:
                    craftObj,ccreated = craft.objects.filter(Q(name=craftName))\
                                .get_or_create(name=craftName,
                                               widthLevel=craftInfo.get('widthLevel'),
                                               craftType = craftInfo.get('craftType'),
                                               minSeats = craftInfo.get('minSeats'),
                                               maxSeats = craftInfo.get('maxSeats')
                                               )

            airlineInfo = flightInfo.get('airlineInfo')
            if airlineInfo is not None:
                airlineCode = airlineInfo.get('code')
                airlineObj = None
                if airlineCode is not None:
                    airlineObj,acreated = airline.objects.filter(Q(code=airlineCode))\
                                .get_or_create(code=airlineCode,
                                               name=airlineInfo.get('name'),
                                               isLCC=airlineInfo.get('isLCC'),
                                               alliance=airlineInfo.get('alliance'),
                                               )

            luggageDirectInfo = flightInfo.get('luggageDirectInfo')
            newflight = flight(dCityCode=flightInfo.get('dCityInfo').get('code'),
                               aCityCode=flightInfo.get('aCityInfo').get('code'),
                               dPortCode=flightInfo.get('dPortInfo').get('code'),
                               aPortCode=flightInfo.get('aPortInfo').get('code'),
                               dTime=flightInfo.get('dDateTime'),
                               aTime=flightInfo.get('aDateTime'),
                               flightNo=flightInfo.get('flightNo'),
                               flightFlag=flightInfo.get('flightFlag'),
                               cabinClass=flightInfo.get('cabinClass'),
                               luggageDirectStatus=luggageDirectInfo.get('directStatus') if luggageDirectInfo is not None else None,
                               luggageDirectDesc=luggageDirectInfo.get('directDesc') if luggageDirectInfo is not None else None,
                               luggageDirectTitle=luggageDirectInfo.get('directTitle') if luggageDirectInfo is not None else None,
                               tripRefId=newtrip.id,
                               airlineRefId=airlineObj.id if airlineObj is not None else None,
                               craftRefId=craftObj.id if craftObj is not None else None,
                               version=version
                               )
            newflight.save()
    # ------------ price -------------------
    policyInfoList = productJson.get('policyInfoList')
    if policyInfoList is not None:
        idx = 0
        for policyInfo in policyInfoList:
            priceDetailInfo = policyInfo.get('priceDetailInfo')
            mainClass = policyInfo.get('mainClass')
            idx = idx + 1
            subId = scheduleSubId+"-"+str(idx)
            if priceDetailInfo is not None:
                adult = priceDetailInfo.get('adult')
                if adult is not None:
                    adultprice, apcreated = price.objects.get_or_create(type='adult',
                                       totalPrice=adult.get('totalPrice'),
                                       tax=adult.get('tax'),
                                       fare=adult.get('fare'),
                                       discount=adult.get('discount'),
                                       mainClass=mainClass,
                                       tripRefId=newtrip.id,
                                       tripSubId=subId,
                                        version=version
                                        )

                child = priceDetailInfo.get('child')
                if child is not None:
                    childprice, cpcreated = price.objects.get_or_create(type='child',
                                       totalPrice=child.get('totalPrice'),
                                       tax=child.get('tax'),
                                       fare=child.get('fare'),
                                       discount=child.get('discount'),
                                       mainClass=mainClass,
                                       tripRefId=newtrip.id,
                                       tripSubId=subId,
                                       version=version
                                       )

                infant = priceDetailInfo.get('infant')
                if infant is not None:
                    infantprice, ipcreated = price.objects.get_or_create(type='infant',
                                       totalPrice=infant.get('totalPrice'),
                                       tax=infant.get('tax'),
                                       fare=infant.get('fare'),
                                       discount=infant.get('discount'),
                                       mainClass=mainClass,
                                       tripRefId=newtrip.id,
                                       tripSubId=subId,
                                       version=version
                                       )


def createSingleFlightProduct(productJson, scheduleSubId):
    cityStopInfoStr=""
    cityStopInfoList = productJson.get('cityStopInfoList')
    if cityStopInfoList is not None:
        for cityStopInfo in cityStopInfoList:
            cityStopInfoStr=cityStopInfoStr+cityStopInfo.get('code')+"|"

    newtrip = trip(departureCityCode=productJson.get('dCityInfo').get('code'),
                   arrivalCityCode=productJson.get('aCityInfo').get('code'),
                   departureTime=productJson.get('dDateTime'),
                   arrivalTime=productJson.get('aDateTime'),
                   cityStopList=cityStopInfoStr,
                   currency=productJson.get('currency'),
                   isShortestDrt=productJson.get('isShortestDrt'),
                   isLowestPrice=productJson.get('isLowestPrice'),
                   durationMin=productJson.get('durationMin'),
                   arrivalDays=productJson.get('arrivalDays'),
                   # scheduleRefId=scheduleDateRef,
                   scheduleSubId=scheduleSubId
                   )
    newtrip.flights=[]
    newtrip.prices={}
    newtrip.airline=None
    newtrip.craft=None
    # newtrip.save()
    # ------------ flight -------------------
    flightInfoList = productJson.get('flightInfoList')
    if flightInfoList is not None:
        for flightInfo in flightInfoList:
            craftInfo = flightInfo.get('craftInfo')
            if craftInfo is not None:
                craftName = craftInfo.get('name')
                craftObj = None
                if craftName is not None:
                    craftObj = craft(name=craftName,
                                     widthLevel=craftInfo.get('widthLevel'),
                                     craftType = craftInfo.get('craftType'),
                                     minSeats = craftInfo.get('minSeats'),
                                     maxSeats = craftInfo.get('maxSeats')
                                     )

            airlineInfo = flightInfo.get('airlineInfo')
            if airlineInfo is not None:
                airlineCode = airlineInfo.get('code')
                airlineObj = None
                if airlineCode is not None:
                    airlineObj = airline(code=airlineCode,
                                         name=airlineInfo.get('name'),
                                         isLCC=airlineInfo.get('isLCC'),
                                         alliance=airlineInfo.get('alliance'),
                                        )

            luggageDirectInfo = flightInfo.get('luggageDirectInfo')
            newflight = flight(dCityCode=flightInfo.get('dCityInfo').get('code'),
                               aCityCode=flightInfo.get('aCityInfo').get('code'),
                               dPortCode=flightInfo.get('dPortInfo').get('code'),
                               aPortCode=flightInfo.get('aPortInfo').get('code'),
                               dTime=flightInfo.get('dDateTime'),
                               aTime=flightInfo.get('aDateTime'),
                               flightNo=flightInfo.get('flightNo'),
                               flightFlag=flightInfo.get('flightFlag'),
                               cabinClass=flightInfo.get('cabinClass'),
                               luggageDirectStatus=luggageDirectInfo.get('directStatus') if luggageDirectInfo is not None else None,
                               luggageDirectDesc=luggageDirectInfo.get('directDesc') if luggageDirectInfo is not None else None,
                               luggageDirectTitle=luggageDirectInfo.get('directTitle') if luggageDirectInfo is not None else None,
                               # tripRefId=newtrip.id,
                               # airlineRefId=airlineObj.id if airlineObj is not None else None,
                               # craftRefId=craftObj.id if craftObj is not None else None,
                               )
            # newflight.save()
            newtrip.flights.append(newflight)
            newtrip.airline = airlineObj
            newtrip.craft = craftObj
    # ------------ price -------------------
    policyInfoList = productJson.get('policyInfoList')
    if policyInfoList is not None:
        idx=0
        for policyInfo in policyInfoList:
            mainClass = policyInfo.get('mainClass')
            priceDetailInfo = policyInfo.get('priceDetailInfo')
            idx = idx + 1
            subId = scheduleSubId+"-"+str(idx)
            if priceDetailInfo is not None:
                priceDetails = {}
                # adult
                adult = priceDetailInfo.get('adult')
                if adult is not None:
                    adultprice = price(type='adult',
                                       totalPrice=adult.get('totalPrice'),
                                       tax=adult.get('tax'),
                                       fare=adult.get('fare'),
                                       discount=adult.get('discount'),
                                       mainClass=mainClass,
                                       # tripRefId=newtrip.id,
                                       tripSubId=subId
                                       )
                    priceDetails['adult'] = adultprice

                # child
                child = priceDetailInfo.get('child')
                if child is not None:
                    childprice = price(type='child',
                                       totalPrice=child.get('totalPrice'),
                                       tax=child.get('tax'),
                                       fare=child.get('fare'),
                                       discount=child.get('discount'),
                                       mainClass=mainClass,
                                       # tripRefId=newtrip.id,
                                       tripSubId=subId
                                       )
                    priceDetails['child'] = childprice

                # infant
                infant = priceDetailInfo.get('infant')
                if infant is not None:
                    infantprice = price(type='infant',
                                       totalPrice=infant.get('totalPrice'),
                                       tax=infant.get('tax'),
                                       fare=infant.get('fare'),
                                       discount=infant.get('discount'),
                                       mainClass=mainClass,
                                       # tripRefId=newtrip.id,
                                       tripSubId=subId
                                       )
                    priceDetails['infant'] = infantprice

                newtrip.prices[subId] = priceDetails
    return newtrip