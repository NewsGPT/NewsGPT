import requests
import json

bing_news_api = "https://api.bing.microsoft.com/v7.0/news/search"

params = "count={}&mkt={}&q={}".format(10, "en-us", "taiwan")

headers = {
    "Ocp-Apim-Subscription-Key": "<NewsAPIKey>"
}

resp = requests.get(bing_news_api, params=params, headers=headers)

with open("test.json", "w") as fout:
    json.dump(resp.json(), fout)
    
d = resp.json()
for idx, i in enumerate(d['value']):
    print(f"\nNews Item: {idx+1}:")
    print(i["name"])
    print(i["description"])
    
#print(resp.json())
