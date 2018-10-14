# coding: utf-8
import sys
import settings
import requests
import json

URL = "https://api.clashroyale.com/v1"


def main():
    access_key = settings.ACCESS_KEY
    target_api = URL+"/players/"
    playerTag = "%2328UGR809L"
    # url = target_api+playerTag+"/upcomingchests"
    url = target_api+playerTag+"/battlelog"
    headers = {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "max-age=60",
        "authorization": "Bearer  %s" % access_key}
    r = requests.get(url, headers=headers)
    data = r.json()
    print(json.dumps(data, indent=4))

if __name__ == '__main__':
    sys.exit(main())
