import requests
import json
import time

coffee_shops = []
params = {}

base_url="https://maps.googleapis.com/maps/api/place/textsearch/json"

query_term="supermarket"
location_value="52.517676414929966,13.384231328158515"
radius_value="2000"
region="de"
key="AIzaSyAACEra83W_p42PXSvJX-h-RMUYEkIKrDY"

endpoint_url=base_url+"?query="+query_term+"&location="+location_value+"&radius="+radius_value+"&region=de"+region+"key="+key
         
res = requests.get(endpoint_url, params = params)
results =  json.loads(res.content)
coffee_shops.extend(results['results'])
time.sleep(2)
while "next_page_token" in results:
     params['pagetoken'] = results['next_page_token'],
     res = requests.get(endpoint_url, params = params)
     results = json.loads(res.content)
     coffee_shops.extend(results['results'])
     time.sleep(2)

f = open("coffee_shops.json", "a")
f.write(json.dumps(coffee_shops))
f.close()

