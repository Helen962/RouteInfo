
import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = "rZqbtpfS5MpHohDoJVC50hLJHQhVJpEt"
BASE_MAPQUEST_URL = "http://open.mapquestapi.com/"


def build_search_url(start:str,ends:str)->str:
    query_parameters = [('key',MAPQUEST_API_KEY),('from',start),('to',ends)]
    return BASE_MAPQUEST_URL +"directions/v2/route?" + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> dict:
    result = None

    try:
        result = urllib.request.urlopen(url)
        json_text = result.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if result != None:
            result.close()



a = build_search_url("Irvine, CA","Lisbon, Portugal")
print(get_result(a))
