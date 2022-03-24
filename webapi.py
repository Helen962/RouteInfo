# Mengchen Xu ID:61281584
# web build module


import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = "rZqbtpfS5MpHohDoJVC50hLJHQhVJpEt"
BASE_MAPQUEST_URL = "http://open.mapquestapi.com/"

# function to build url
def build_search_url(start:str,ends:str)->str:
    query_parameters = [('key',MAPQUEST_API_KEY),('from',start),('to',ends)]
    return BASE_MAPQUEST_URL +"directions/v2/route?" + urllib.parse.urlencode(query_parameters)

# function that get the web result(dictionary)of MAPQUEST
def get_result(url: str) -> dict:
    result = None
    try:
        result = urllib.request.urlopen(url)
        json_text = result.read().decode(encoding = 'utf-8')
#        print(json_text)
        return json.loads(json_text)

    finally:
        if result != None:
            result.close()

# function that build latitude and longtitude str for finding elevation
def build_latlng(search_result:dict,state:int)->str:
    latlng = ""
    for item in search_result['route']['legs']:
        lati = item['maneuvers'][state]['startPoint']['lat']
        long = item['maneuvers'][state]['startPoint']['lng']
        latlng = str(lati)+","+str(long)
    return latlng

# function for build url to find elevation
def build_elev_url(latlng:str)->str:
    query_parameters = [('key',MAPQUEST_API_KEY),('shapeFormat','raw'),
                        ('latLngCollection',latlng)]
    return BASE_MAPQUEST_URL + "elevation/v1/profile?" + urllib.parse.urlencode(query_parameters)

# function to get elevation result dict from MAPQUEST
def get_elev(url: str) -> dict:
    result = None
    try:
        result = urllib.request.urlopen(url)
        json_text = result.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if result != None:
            result.close()

# function that combines all the functions to find elevtion 
def combine_result(search_result,state)->dict:
    latlong = build_latlng(search_result,state)
    url = build_elev_url(latlong)
    result = get_elev(url)
    return result

