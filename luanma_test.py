# -*- coding: utf-8 -*-

import json
import os
import requests

girl = {'name':'推女郎','nickname':'赵惟依','catalog':'tuigirl',"issue": 175, "pictureCount": 24}
girls = [girl]

# print(girls)

# with open('test.json','w') as f:
#     f.write(json.dumps(girls))
#     f.close()

with open('test.json','r') as f:
    data = json.load(f)
    f.close()

print(data)

url = 'http://tuigirl-1254818389.cosbj.myqcloud.com/picture/{catalog}/{issue}/{pictureCount}.jpg'
directory = os.path.join('data',data[0]['name'],'{}-{}'.format(data[0]['issue'],data[0]['nickname']))
file_path = os.path.join(directory,'{}.jpg'.format(1))

if not os.path.exists(directory):
    try:
        os.makedirs(directory)
    except Exception as e:
        print(e)

image = requests.get(url.format(catalog=data[0]['catalog'],issue=data[0]['issue'],pictureCount=1))

with open(file_path,'wb') as f:
    f.write(image.content)
    f.close()