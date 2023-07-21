from os import path
import json
import requests
import execjs

cookies = {
    'btoken': '7OACYBSAZ0CUPKBIQDTF33BTQ72C554B',
    'hy_data_2020_id': '18973acd4be808-08b941ae14f31e-1b525634-2007040-18973acd4bff84',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218973acd4be808-08b941ae14f31e-1b525634-2007040-18973acd4bff84%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218973acd4be808-08b941ae14f31e-1b525634-2007040-18973acd4bff84%22%7D',
    'sajssdk_2020_cross_new_user': '1',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,ru;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'btoken=7OACYBSAZ0CUPKBIQDTF33BTQ72C554B; hy_data_2020_id=18973acd4be808-08b941ae14f31e-1b525634-2007040-18973acd4bff84; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218973acd4be808-08b941ae14f31e-1b525634-2007040-18973acd4bff84%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218973acd4be808-08b941ae14f31e-1b525634-2007040-18973acd4bff84%22%7D; sajssdk_2020_cross_new_user=1',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiniudata.com/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

json_data = {
    'payload': 'LBcwWVcHInhydGB7AHJmZRAnX05ccG4HMA==',
    'sig': '245F759E0522F7E7CBA13F5AFBA997E9',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_home/list_home_tag_company',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
data = '{"payload":"LBcwWVcHInhydGB7AHJmZRAnX05ccG4HMA==","sig":"245F759E0522F7E7CBA13F5AFBA997E9","v":1}'
response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_home/list_home_tag_company',
    cookies=cookies,
    headers=headers,
    data=data,
).json()


def json_path(p: str):
    return path.join(path.dirname(__file__), p)


with open(json_path('dd.js'), 'r') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
result = ctx.call('dd', response['d'])
data = json.loads(result)['list']
print(data)
