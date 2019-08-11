import requests

def getHTTPRequest(url):
    try:
        response=requests.get(url)
        response.raise_for_status()#if status code is not 200, then gernate HttpError
        response.encoding=response.apparent_encoding
        return response.text
    except:
        print ("Error generate")


if __name__ =='__main__':
    url="movie.douban.com/top250"
    print(getHTTPRequest(url))