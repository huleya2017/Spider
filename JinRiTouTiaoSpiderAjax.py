import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
import datetime


def get_page(offset):
    headers = {
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'user - agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': ' 街拍',
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
    }

    cookies = {'tt_webid': '673187957437946419', 'WEATHER_CITY': '%E5%8C%97%E4%BA%AC',
               'tt_webid': '6731879574379464199', 'csrftoken': 'ef78aba216713b4b5507510843bb2c3b',
               's_v_web_id': '33a51767b36abf5cb2f659b38af15c3d', '__tasessionId': 't8av7ix8v1567398609081'}

    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        if response.status_code == 200:
            return response.json()
    except  requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        itemList = []
        for item in json.get('data'):
            if item.get('title') is None or item.get('image_list') is None:  # if content is none,continue directly
                continue
            else:
                title = item.get('title')
                images = item.get('image_list')
                lis = []
                dic = {}
                for image in images:
                    url = image.get('url')
                    lis.append(url)
                dic = dict(title=title, image=lis)
                itemList.append(dic)
        return itemList


def save_images(item):
    title = item.get('title')
    if title.find('/') >= 0:  # if title contains '/',use mkdir will not create folder
        title = title.replace('/', '')

    if not os.path.exists(title):
        os.mkdir(title)

    for url in item.get('image'):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                file_path = '{0}/{1}.{2}'.format(title, md5(response.content).hexdigest(), 'jpg')
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                else:
                    print('Image already download', file_path)
        except requests.ConnectionError:
            print('Failed to save images')


def main(offset):
    json = get_page(offset)
    items = get_images(json)
    for item in items:
        print(item)
        save_images(item)


GROUP_START = 1
GROUP_END = 4

if __name__ == '__main__':
    start = datetime.datetime.now()
    #mutiple process
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()

    #dan process
    # groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    # for offset in groups:
    #     main(offset)

    end = datetime.datetime.now()

    print((end - start).seconds)
