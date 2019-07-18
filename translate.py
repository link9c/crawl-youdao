'''
有道翻译反反爬虫
2019 07/18更新salt，bv规则
sign: md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
bv:md5("5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36")

'''

import requests
import time
import random
import hashlib
import json


def generate_md5(string):
    '''
    python3中文本字符串和字节字符串是严格区分的，默认为unicode格式的文本字符串,
    因为默认的文本字符串为unicode格式，因此文本字符串没有decode方法,
    encode('utf-8') 将文本字符串编码，转换为已编码的字节字符串类型.
    '''
    st = string.encode('utf-8')
    md5 = hashlib.md5(st).hexdigest()
    return md5

def translated_get(word):
    # 两种版本的网址
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    ua = "5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    e = word.replace('\n', '')

    t = generate_md5(ua)
    bv = t

    r = str(int(time.time()*1000))
    ts = r


    salt = r + str(random.randint(0,9))
    sign = generate_md5("fanyideskweb" + e + salt + "n%A-rKaT5fb[Gy?;N5@Tj")
    # form data
    data = {
    'i': e,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': salt,
    'sign': sign,
    'ts': ts,
    'bv': bv,
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
    }

    header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '%d' % len(word) ,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1531297858@106.2.43.11; OUTFOX_SEARCH_USER_ID_NCOO=1878656658.6952307; UM_distinctid=167cbe876e53cd-03535e9814391c-58422116-144000-167cbe876e6e81; _ntes_nnid=d0b5634f521fef3de304ef964df9bdad,1551178986167; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcymbI30lnopcrxsxPTw; ___rl__test__cookies=1560856146058',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    # 'smartresult': 'dict',
    # 'smartresult': 'rule',
    }

    res = requests.post(url, data=data, headers=header)

    search_result = res.content.decode('utf-8')
    data = json.loads(search_result)
    # print(data)
    simple = []
    complete = []
    if not 'smartResult' in data:
        for t in range(len(data['translateResult'][0])):
            simple.append(data['translateResult'][0][t]['tgt'])
    else:
        for t in range(len(data['translateResult'][0])):
            simple.append(data['translateResult'][0][t]['tgt'])
            for t in range(len(data['smartResult']['entries'])):
                complete.append(data['smartResult']['entries'][t])
    return ''.join(simple) + '\n' + ''.join(complete)

