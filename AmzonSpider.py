import requests

"""when headers user-agent is not common web browser name, then need give headers user-agent Mozilla/5.0"""

def getHTTPRequest(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        response=requests.get(url,headers=kv)
        print(response.request.headers)
        response.raise_for_status()#if status code is not 200, then gernate HttpError
        response.encoding=response.apparent_encoding
        return response.text[:100]
    except:
        print (response.status_code)
        print ("Error generate")


if __name__ =='__main__':
    url="https://www.amazon.cn/dp/B003DQPBXE?ref_=Oct_DLandingSV2_PC_a50a1668_2&smid=A2EDK7H33M5FFG"
    print(getHTTPRequest(url))