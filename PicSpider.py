import requests
import os

"""spider a pic and save it"""

def getHTTPRequest(root,path,url):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            response=requests.get(url)
            with open(path,'wb') as f:
                f.write(response.content)
                f.close()
                print("Save pic successfully")
        else:
            print("Pic exists")
    except:
        print ("Spider pic fail")


if __name__ =='__main__':
    url="http://image.ngchina.com.cn/2019/0808/20190808062340446.jpg"
    root='/Users/pt/workspace/Spider/'
    path=root+url.split('/')[-1]
    print(getHTTPRequest(root,path,url))
