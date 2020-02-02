import json
import requests
import urllib
import shutil
import jwt

def get_pages():
    url = 'https://lib-nuanxin.wqxuetang.com/v1/read/initread?bid=3207680'
    r = requests.get(url)
    book_details = r.json()

    return book_details['data']['pages']

def get_payload():
    url = 'https://lib-nuanxin.wqxuetang.com/v1/read/k?bid=2175744'
    r = requests.get(url)
    payload = r.json()['data']

    return payload

def gen_jwt(payload):
    pay = {}
def main():
   # for page in pages:
    url = 'https://lib-nuanxin.wqxuetang.com/page/img/3207680/2?k=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwIjoyLCJ0IjoxNTgwNjU1OTA2MDAwLCJiIjoiMzIwNzY4MCIsInciOjEwMDAsImsiOiJ7XCJ1XCI6XCJNNkZkaEFwWU55dz1cIixcImlcIjpcIm0waTRUYmZ2SmZoOFZTVUhqaUZuNkE9PVwiLFwidFwiOlwiTGZFUUdNMWoxT3JCazBvZmJBdFROUT09XCIsXCJiXCI6XCJIZnFSYmZpdjkvVT1cIixcIm5cIjpcIlFaZDhHaGVXWUU0PVwifSIsImlhdCI6MTU4MDY1NTkwNn0.SkU6Dfoj3YriSWZLWWqrbZc86VEH5ErfZMP3Ktced0s'
    response = requests.get(url, headers={'referer': 'https://lib-nuanxin.wqxuetang.com/read/pdf/3207680'})
    with open('2.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

get_payload()