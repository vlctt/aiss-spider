# -*- coding: utf-8 -*-
import requests
import json

url = 'http://api.pmkoo.cn/aiss/suite/suiteList.do'
girl_jsons = []
page = 1
while True:
    params = {'page': page, 'userId': 153044}
    response = requests.post(url, data=params)
    data = response.json()
    # print(len(data['data']['list']))
    girls = data['data']['list']
    if not girls:
        break
    # print(data['data']['list'])
    # girl = girls[0]
    for girl in girls:
        catalog = girl['source']['catalog']
        issue = girl['issue']
        pictureCount = girl['pictureCount']
        name = girl['source']['name']
        nickname = girl['author']['nickname']

        girl_json = {}
        girl_json['name'] = name
        girl_json['nickname'] = nickname
        girl_json['catalog'] = catalog
        girl_json['issue'] = issue
        girl_json['pictureCount'] = pictureCount

        girl_jsons.append(girl_json)

    page += 1

        # print(girl_json)

with open('girls.json','w') as f:
    f.write(json.dumps(girl_jsons))
    f.close()