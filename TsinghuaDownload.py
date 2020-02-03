import json
import requests
import os
import jwt
from datetime import datetime


def get_timestamp():
    now = datetime.now().replace(microsecond=0)
    timestamp = datetime.timestamp(now)

    return timestamp


def get_pages():
    url = 'https://lib-nuanxin.wqxuetang.com/v1/read/initread?bid=3208401'
    r = requests.get(url)
    book_details = r.json()

    return book_details['data']['pages']


def get_payload():
    url = 'https://lib-nuanxin.wqxuetang.com/v1/read/k?bid=3208401'
    r = requests.get(url)
    payload = r.json()['data']

    return payload


def gen_jwt(payload, page):
    timestamp = int(get_timestamp())
    k = json.dumps(payload)
    k.replace('"', '\\"')
    jwt_secret = 'g0NnWdSE8qEjdMD8a1aq12qEYphwErKctvfd3IktWHWiOBpVsgkecur38aBRPn2w'
    pay = {'p': page,
           't': timestamp * 1000,
           'b': '3208401',
           'w': 1000,
           'k': k,
           'iat': timestamp}
    encode = jwt.encode(pay, jwt_secret, algorithm='HS256').decode('utf-8')

    return encode


def get_book():
    pages = get_pages()
    if not os.path.exists("3208401"):
        os.mkdir("3208401")
    for page in range(1, int(pages) + 1):
        if os.path.isfile("3208401/{}.jpg".format(page)):
            continue
        jwtencoded = gen_jwt(get_payload(), str(page))
        imgurl = 'https://lib-nuanxin.wqxuetang.com/page/img/3208401/{}?k='.format(str(page))
        url = imgurl + jwtencoded
        headers = {'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5',
                   'referer': 'https://lib-nuanxin.wqxuetang.com/read/pdf/3208401',
                   'sec-fetch-mode': 'no-cors',
                   'sec-fetch-site': 'same-origin',
                   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
        response = requests.get(url, headers=headers)
        with open('3208401/{}.jpg'.format(str(page)), 'wb') as f:
            f.write(response.content)
            print("Saving page {}".format(str(page)))

        f.close()
# print(gen_jwt(get_payload()))
if __name__ == '__main__':
    get_book()
