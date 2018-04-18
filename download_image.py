# -*- coding: utf-8 -*-

import json
import requests
import os
from multiprocessing import Pool
import time

def get_data():
    with open('girls.json', 'r') as f:
        data = json.load(f)
        f.close()
    return data

def make_directory(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except Exception as e:
            print(e)
    return True

def get_image_url(data):
    req_urls = []
    base_url = 'http://tuigirl-1254818389.cosbj.myqcloud.com/picture/{catalog}/{issue}/{pic_ord}.jpg'
    for girl in data:
        name = girl['name']
        nickname = girl['nickname']
        pictureCount = girl['pictureCount']
        catalog = girl['catalog']
        issue = girl['issue']

        for idx in range(0, pictureCount):
            url = base_url.format(catalog=catalog, issue=issue, pic_ord=idx)
            directory = os.path.join('data', name, '{}-{}'.format(issue, nickname))
            file_path = os.path.join(directory, '{}.jpg'.format(idx))

            req_urls.append((url, directory, file_path))

    return req_urls

def download_image(req_url):
    url,directory,file_path = req_url

    if os.path.exists(file_path):
        print("exists")
        return

    make_directory(directory)

    image = requests.get(url)

    with open(file_path,'wb') as f:
        f.write(image.content)
        f.close()

def multi_process_image(req_urls,processes=10):
    start_time = time.time()

    pool = Pool(processes)

    for req_url in req_urls:
        pool.apply_async(download_image,(req_url,))

    pool.close()
    pool.join()
    end_time = time.time()
    print('下载完毕,用时:%s秒' % (end_time - start_time))

if __name__ == '__main__':
    data = get_data()
    req_urls = get_image_url(data)
    multi_process_image(req_urls)
