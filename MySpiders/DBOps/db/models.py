#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
try:
    from django.db import models
except Exception:
    print("Exception: Django Not Found, please install it with \"pip install django\".")
    sys.exit()


# model
class POIInfo(models.Model):
    ID = models.AutoField(primary_key=True)
    poiId = models.TextField()
    cityCode = models.TextField()
    cityName = models.TextField()
    cityEName = models.TextField()
    name = models.TextField()
    countryName = models.TextField()
    countryCode = models.TextField()
    distance = models.IntegerField()
    isDomestic = models.BooleanField(default=False)
    isCanSelect = models.BooleanField(default=False)
    airportCode = models.TextField()
    provinceName = models.TextField()
    provinceCode = models.TextField()
    mapWord = models.TextField()
    dataType = models.IntegerField()
    airportShortName = models.TextField()
    virtualRegionCode = models.TextField()
    timeZone = models.IntegerField()
    poiParentId = models.IntegerField()

    class Meta:
        db_table = "POIInfo"
        managed = False

    def __str__(self):
        return self.name

    __repr__ = __str__

class Response(models.Model):
    id = models.AutoField(primary_key=True)
    departureCityCode = models.TextField()
    arrivalCityCode = models.TextField()
    scheduleDate = models.DateField()
    respData = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    version = models.TextField()

    class Meta:
        db_table = "response"

    def __str__(self):
        return self.departureCityCode +"-"+self.arrivalCityCode+" "+str(self.scheduleDate)

    __repr__ = __str__

class schedule(models.Model):
    id = models.AutoField(primary_key=True)
    departureCityCode = models.TextField()
    arrivalCityCode = models.TextField()
    scheduleDate = models.DateField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    bizId = models.TextField()
    version = models.TextField()
    status = models.TextField()
    errorReason = models.TextField()

    trips=[]

    class Meta:
        db_table = "schedule"

    def __str__(self):
        return self.departureCityCode +"-"+self.arrivalCityCode+" "+str(self.scheduleDate)

    __repr__ = __str__

class trip(models.Model):
    id = models.AutoField(primary_key=True)
    scheduleSubId = models.TextField()
    departureCityCode = models.TextField()
    arrivalCityCode = models.TextField()
    departureTime = models.BigIntegerField()
    arrivalTime = models.BigIntegerField()
    currency=models.TextField()
    isShortestDrt = models.BooleanField(default=False)
    isLowestPrice = models.BooleanField(default=False)
    durationMin = models.IntegerField(null=True)
    arrivalDays = models.IntegerField(null=True)
    cityStopList = models.TextField(null=True) #使用'|'分隔多个citystop
    scheduleRefId = models.IntegerField()
    version = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    flights = []
    prices = {}
    airline = None
    craft = None

    class Meta:
        db_table = "trip"

    def __str__(self):
        return self.departureCityCode +"-"+self.arrivalCityCode+" "+str(self.departureTime)+"-"+str(self.arrivalTime)

    __repr__ = __str__

class flight(models.Model):
    id = models.AutoField(primary_key=True)
    dCityCode = models.TextField()
    aCityCode = models.TextField()
    dPortCode = models.TextField(null=True)
    aPortCode = models.TextField(null=True)
    dTime = models.BigIntegerField()
    aTime = models.BigIntegerField()
    flightNo = models.TextField()
    flightFlag = models.TextField()
    cabinClass = models.TextField()
    luggageDirectStatus = models.TextField(null=True)
    luggageDirectDesc = models.TextField(null=True)
    luggageDirectTitle = models.TextField(null=True)
    tripRefId = models.IntegerField()
    airlineRefId = models.IntegerField(null=True)
    craftRefId = models.IntegerField(null=True)
    version = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "flight"

    def __str__(self):
        return self.dCityCode+":"+self.dPortCode+" - "+self.aCityCode+":"+self.aPortCode+" "+str(self.flightNo)

    __repr__ = __str__

class price(models.Model):
    id = models.AutoField(primary_key=True)
    tripSubId = models.TextField()
    type = models.TextField() # adult/child/infant
    totalPrice = models.FloatField()
    tax = models.FloatField(null=True)
    fare = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    mainClass = models.TextField()
    tripRefId = models.IntegerField()
    version = models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "price"

    def __str__(self):
        return self.type +":"+str(self.totalPrice)

    __repr__ = __str__

class craft(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    widthLevel = models.TextField() #单走道/多走道
    craftType = models.TextField()
    minSeats = models.IntegerField()
    maxSeats = models.IntegerField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "craft"

    def __str__(self):
        return self.name

    __repr__ = __str__

class airline(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField()
    name = models.TextField(null=True)
    isLCC = models.BooleanField(default=False)
    alliance = models.TextField(null=True)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "airline"

    def __str__(self):
        return self.name

    __repr__ = __str__
