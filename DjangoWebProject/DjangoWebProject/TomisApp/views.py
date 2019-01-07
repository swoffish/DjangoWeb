from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import json
import itertools
import collections
from TomisApp import models
from operator import itemgetter




def index(request):
   tomis_data = json.loads(open('TomisApp/static/TomisDB.json').read())
   tomis_sorted = sorted(tomis_data, key=itemgetter('Device'))
   keys = []
   deviceCount = []
   clickCount = []
   impCount = []
   groupByDeviceList = []
   for key, group in itertools.groupby(tomis_sorted, key=lambda x:x['Device']):
        keys.append(key)
        groupByDeviceList.append(dict(device=key, tomis_item=list(group)))
     
    # Counts your devices
   for deviceCounter in groupByDeviceList:
        deviceCount.append(len(deviceCounter["tomis_item"]))
    
   return render(
        request,
        "index.html",  
        {
            'categories' : keys,
            'counts' : deviceCount
             
        }
    )




def ByDevice(request):
     tomis_data = json.loads(open('TomisApp/static/TomisDB.json').read())
     tomis_sorted = sorted(tomis_data, key=itemgetter('Device'))
     keys = []
     deviceCount = []
     clickCount = []
     impCount = []
     interactCount = []
     groupByDeviceList = []
     for key, group in itertools.groupby(tomis_sorted, key=lambda x:x['Device']):
         keys.append(key)
         groupByDeviceList.append(dict(device=key, tomis_item=list(group)))
     
     # Counts your devices
     for deviceCounter in groupByDeviceList:
         deviceCount.append(len(deviceCounter["tomis_item"]))
         
     # Counts clicks
     
     for clickCounter in groupByDeviceList:
        thisClickCounter = 0
        thisImpCounter = 0
        thisIntCounter = 0
        for clicks in clickCounter["tomis_item"]:
            thisClickCounter = thisClickCounter + int(clicks.get("Clicks"))
            thisImpCounter = thisImpCounter + int(clicks.get("Impressions"))
            thisIntCounter = thisIntCounter + int(clicks.get("Interactions"))
        clickCount.append(thisClickCounter)
        impCount.append(thisImpCounter)
        interactCount.append(thisIntCounter)
       


     return render(
        request,
        "ByDevice.html",  
        {
            'categories' : keys,
            'interactions' : interactCount,
            'clicks' : clickCount,
            'impressions' : impCount
        }
    )


def ByLocationType(request):
     tomis_data = json.loads(open('TomisApp/static/TomisDB.json').read())
     tomis_sorted = sorted(tomis_data, key=itemgetter('LocationType'))
     keys = []
     deviceCount = []
     clickCount = []
     impCount = []
     interactCount = []
     groupByDeviceList = []
     for key, group in itertools.groupby(tomis_sorted, key=lambda x:x['LocationType']):
         keys.append(key)
         groupByDeviceList.append(dict(device=key, tomis_item=list(group)))
     
     # Counts your devices
     for deviceCounter in groupByDeviceList:
         deviceCount.append(len(deviceCounter["tomis_item"]))
         
     # Counts clicks
     
     for clickCounter in groupByDeviceList:
        thisClickCounter = 0
        thisImpCounter = 0
        thisIntCounter = 0
        for clicks in clickCounter["tomis_item"]:
            thisClickCounter = thisClickCounter + int(clicks.get("Clicks"))
            thisImpCounter = thisImpCounter + int(clicks.get("Impressions"))
            thisIntCounter = thisIntCounter + int(clicks.get("Interactions"))
        clickCount.append(thisClickCounter)
        impCount.append(thisImpCounter)
        interactCount.append(thisIntCounter)
       


     return render(
        request,
        "ByLocationType.html",  
        {
            'categories' : keys,
            'interactions' : interactCount,
            'clicks' : clickCount,
            'impressions' : impCount
        }
    )

