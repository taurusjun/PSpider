#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from prettytable import PrettyTable
import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Content-Type": "application/json",  # 声明文本类型为 json 格式
    # "referer": r"https://flights.ctrip.com/itinerary/oneway/hak-khn?date=2018-11-11"
}

url_cities= 'https://flights.ctrip.com/international/search/api/country/getCountryCodes';
# response = requests.get(url_cities, headers=headers).text

url_search_LowPrice = 'https://flights.ctrip.com/international/search/api/recommend/adjacentLowPrice/getAdjacentCityLowPrice?v=0.8733866155475722'
# request_payload={
#     "flightWayEnum": "OW",
#     "arrivalProvinceId": 0,
#     "extGlobalSwitches":
#     {
#         "useAllRecommendSwitch": "true"
#     },
#     "arrivalCountryName": "韩国",
#     "infantCount": 0,
#     "cabin": "Y_S",
#     "cabinEnum": "Y_S",
#     "departCountryName": "中国",
#     "flightSegments": [
#     {
#         "departureDate": "2019-10-20",
#         "arrivalProvinceId": 0,
#         "arrivalCountryName": "韩国",
#         "departureCityName": "上海",
#         "departureCityCode": "SHA",
#         "departureCountryName": "中国",
#         "arrivalCityName": "首尔",
#         "arrivalCityCode": "SEL",
#         "departureCityTimeZone": 480,
#         "arrivalCountryId": 42,
#         "timeZone": 480,
#         "departureCityId": 2,
#         "departureCountryId": 1,
#         "arrivalCityTimeZone": 540,
#         "departureProvinceId": 2,
#         "arrivalCityId": 274
#     }],
#     "childCount": 0,
#     "adultCount": 1,
#     "extensionAttributes":
#     {
#         "isFlightIntlNewUser": "false"
#     },
#     "transactionID": "b1d862cd19994683934ee1e53bdfdba8",
#     "directFlight": "false",
#     "departureCityId": 2,
#     "isMultiplePassengerType": 0,
#     "flightWay": "S",
#     "arrivalCityId": 274,
#     "departProvinceId": 2,
#     "flightSegmentList": [
#     {
#         "departureDate": "2019-10-20",
#         "arrivalProvinceId": 0,
#         "arrivalCountryName": "韩国",
#         "departureCityName": "上海",
#         "departureCityCode": "SHA",
#         "departureCountryName": "中国",
#         "arrivalCityName": "首尔",
#         "arrivalCityCode": "SEL",
#         "departureCityTimeZone": 480,
#         "arrivalCountryId": 42,
#         "timeZone": 480,
#         "departureCityId": 2,
#         "departureCountryId": 1,
#         "arrivalCityTimeZone": 540,
#         "departureProvinceId": 2,
#         "arrivalCityId": 274
#     }]
# }
request_payload={
    # "flightWayEnum": "OW",
    # "arrivalProvinceId": 0,
    # "extGlobalSwitches":
    # {
    #     "useAllRecommendSwitch": "true"
    # },
    # "arrivalCountryName": "韩国",
    # "infantCount": 0,
    # "cabin": "Y_S",
    # "cabinEnum": "Y_S",
    # "departCountryName": "中国",
    # "flightSegments": [
    # {
    #     "departureDate": "2019-10-20",
    #     "arrivalProvinceId": 0,
    #     "arrivalCountryName": "韩国",
    #     "departureCityName": "上海",
    #     "departureCityCode": "SHA",
    #     "departureCountryName": "中国",
    #     "arrivalCityName": "首尔",
    #     "arrivalCityCode": "SEL",
    #     "departureCityTimeZone": 480,
    #     "arrivalCountryId": 42,
    #     "timeZone": 480,
    #     "departureCityId": 2,
    #     "departureCountryId": 1,
    #     "arrivalCityTimeZone": 540,
    #     "departureProvinceId": 2,
    #     "arrivalCityId": 274
    # }],
    "childCount": 1,
    "adultCount": 2,
    # "extensionAttributes":
    # {
    #     "isFlightIntlNewUser": "false"
    # },
    # "transactionID": "b1d862cd19994683934ee1e53bdfdba8",
    "directFlight": "true",
    # "departureCityId": 2,
    # "isMultiplePassengerType": 0,
    # "flightWay": "S",
    # "arrivalCityId": 274,
    # "departProvinceId": 2,
    "flightSegmentList": [
    {
        "departureDate": "2019-10-20",
        # "arrivalProvinceId": 0,
        # "arrivalCountryName": "韩国",
        # "departureCityName": "上海",
        "departureCityCode": "SHA",
        "departureCountryName": "中国",
        "arrivalCityName": "首尔",
        "arrivalCityCode": "SEL",
        "departureCityTimeZone": 480,
        "arrivalCountryId": 42,
        "timeZone": 480,
        "departureCityId": 2,
        "departureCountryId": 1,
        "arrivalCityTimeZone": 540,
        "departureProvinceId": 2,
        "arrivalCityId": 274
    }]
}
# response = requests.post(url_search_LowPrice, data=json.dumps(request_payload), headers=headers).text

# 按天取得半年内出发-到达的最低价航班, 返回值中只有价格和总价，没有出发和到达时间
url_calenda_list='https://flights.ctrip.com/international/search/api/lowprice/calendar/getCalendarDetailList'
request_payload_calenda_list={
    "cabin": "Y_S",
    "flightWay": "S",
    "flightSegmentList": [
    {
        "arrivalCityCode": "SEL",
        "departureCityCode": "SHA",
        "departureDate": "2019-10-20"
    }]
}
# response = requests.post(url_calenda_list, data=json.dumps(request_payload_calenda_list), headers=headers).text

###############################

# prepare, 获取可用的航班信息（无价格）
url_search_prepare = 'https://flights.ctrip.com/international/search/api/flightlist/round-sha-syd?depdate=2019-10-25_2019-11-29&cabin=y_s&adult=2&child=0&infant=0&v=0.16121281722847125'
# response = requests.get(url_search_prepare, headers=headers).text


# 全量搜索
url_batch_search = 'https://flights.ctrip.com/international/search/api/search/batchSearch?v=0.7324365477529182'
headers_batch_search = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Content-Type": "application/json",  # 声明文本类型为 json 格式
    # "referer": r"https://flights.ctrip.com/itinerary/oneway/hak-khn?date=2018-11-11",
    # "sign": "9b13b87a90f91c6b5817e8dfb7495489",
    "sign": "9b13b87a90f91c6b5817e8dfb7495489",
    "transactionid": "3d3c60dd93814acd95aa358991f55b28"
}
request_payload_batch_search={
    "flightWayEnum": "OW",
    "arrivalProvinceId": 0,
    "extGlobalSwitches":
    {
        "useAllRecommendSwitch": "true"
    },
    "arrivalCountryName": "韩国",
    "infantCount": 0,
    "cabin": "Y_S",
    "cabinEnum": "Y_S",
    "departCountryName": "中国",
    "flightSegments": [
    {
        "departureDate": "2019-10-20",
        "arrivalProvinceId": 0,
        "arrivalCountryName": "韩国",
        "departureCityName": "上海",
        "departureCityCode": "SHA",
        "departureCountryName": "中国",
        "arrivalCityName": "首尔",
        "arrivalCityCode": "SEL",
        "departureCityTimeZone": 480,
        "arrivalCountryId": 42,
        "timeZone": 480,
        "departureCityId": 2,
        "departureCountryId": 1,
        "arrivalCityTimeZone": 540,
        "departureProvinceId": 2,
        "arrivalCityId": 274
    }],
    "childCount": 0,
    "segmentNo": 1,
    "adultCount": 1,
    "extensionAttributes":
    {
        "isFlightIntlNewUser": "false"
    },
    "transactionID": "3d3c60dd93814acd95aa358991f55b28",
    "directFlight": "false",
    "departureCityId": 2,
    "isMultiplePassengerType": 0,
    "flightWay": "S",
    "arrivalCityId": 274,
    "departProvinceId": 2
}

response = requests.post(url_batch_search, data=json.dumps(request_payload_batch_search), headers=headers_batch_search).text

## TODO
## 1. POST
## https://flights.ctrip.com/international/search/api/flight/comfort/batchGetComfortTagList
## 2. POST
## 取得45天内的航班细节
## https://flights.ctrip.com/international/search/api/lowprice/calendar/get45DaysCalendarDetailList
## payload:
# {
#     "flightSegmentList": [
#     {
#         "arrivalCityCode": "SYD",
#         "departureCityCode": "SHA",
#         "departureDate": "2019-10-20"
#     },
#     {
#         "arrivalCityCode": "SHA",
#         "departureCityCode": "SYD",
#         "departureDate": "2019-11-20"
#     }],
#     "cabin": "Y_S",
#     "flightWay": "D"
# }

print(response)