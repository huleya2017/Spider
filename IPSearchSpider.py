import requests
import os

"""Spider IP with API"""

def getHTTPRequest(url):
    try:
        response=requests.get(url+'202.204.80.112')
        response.raise_for_status()
        print(response.status_code)
    except:
        print ("Spider fail")


if __name__ =='__main__':
    url="http://m.ip138.com/ip.asp?ip=" #API path
    print(getHTTPRequest(url))
