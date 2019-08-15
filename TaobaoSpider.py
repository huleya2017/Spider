import requests
import re

def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(iList,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            iList.append([price,title])
    except:
        print("")

def printGoodList(iList):
    template="{:4}\t{:8}\t{:16}"
    print(template.format("序号","价格","名称"))
    count=0
    for g in iList:
        count=count+1
        print(template.format(count,g[0],g[1]))


def main():
    goods="书包"
    depth=2
    start_url='https://s.taobao.com/search?q='+goods
    inforList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            print(url)
            html=getHtmlText(url)
            parsePage(inforList,html)
        except:
            continue
    printGoodList(inforList)

main()


