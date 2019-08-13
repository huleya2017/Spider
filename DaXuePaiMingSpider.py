import requests
import bs4
from bs4 import BeautifulSoup

def getHtmlContent(ulr):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(univList,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr.find_all('td')
            univList.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(univList,num):
    template="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(template.format("排名","学校名称","学校省份",chr(12288)))
    for i in range(num):
        u=univList[i]
        print(template.format(u[0], u[1],u[2],chr(12288)))
    print("Suc" + str(num))

if __name__=="__main__":
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    univList=[]
    html=getHtmlContent(url)
    fillUnivList(univList,html)
    printUnivList(univList,20)
