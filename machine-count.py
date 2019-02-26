# -*- coding: utf-8 -*-
import requests
import json

def dealJson(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    json = requests.get(url, headers=header).content
    return json

if __name__ == '__main__':

    jsonStr = dealJson('')
    text = json.loads(jsonStr)

    print len(text['data'])

