import requests
from bs4 import *


url='https://movie.douban.com/top250'
para_data=requests.get(url)
soup=BeautifulSoup(para_data.text,'lxml')

titles=soup.select('div.hd>a')
rates=soup.select('span.rating_num')
imgs=soup.select('img[width="100"]')

for tile,rate,img in zip(titles,rates,imgs):
    data={
        'tile':list(tile.stripped_strings),
        'rate':rate.get_text(),
        'img':img.get('src')
    }
    print (data)
