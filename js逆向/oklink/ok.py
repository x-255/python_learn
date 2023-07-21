from os import path
import requests
import execjs

cookies = {
    'locale': 'zh_CN',
    'devId': '4931f7e6-d0fb-44ff-b0d3-6a252bacdccb',
    'first_ref': 'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D5BfrIVExB8-u3E1B_Dc14oA3N2Fa-I0c954vDb0U-KNIF3FSOU2fJ61w4FHkEuva%26wd%3D%26eqid%3Df82ef364000bc34e0000000464ba5ad4',
    'aliyungf_tc': 'b6229c36b7b507b7a2625e94e8badf449acb20ddf73bd5a75b80897570312291',
    'okg.currentMedia': 'lg',
    '_monitor_extras': '{"deviceId":"ewWrX5o7kAGso900zMsZ75","eventId":12,"sequenceNumber":12}',
}


def json_path(p: str):
    return path.join(path.dirname(__file__), p)


with open(json_path('ok.js'), 'r') as f:
    js = f.read()
key = execjs.compile(js).call('getApiKey')

headers = {
    'authority': 'www.oklink.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN',
    'app-type': 'web',
    'cache-control': 'no-cache',
    # 'cookie': 'locale=zh_CN; devId=4931f7e6-d0fb-44ff-b0d3-6a252bacdccb; first_ref=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D5BfrIVExB8-u3E1B_Dc14oA3N2Fa-I0c954vDb0U-KNIF3FSOU2fJ61w4FHkEuva%26wd%3D%26eqid%3Df82ef364000bc34e0000000464ba5ad4; aliyungf_tc=b6229c36b7b507b7a2625e94e8badf449acb20ddf73bd5a75b80897570312291; okg.currentMedia=lg; _monitor_extras={"deviceId":"ewWrX5o7kAGso900zMsZ75","eventId":12,"sequenceNumber":12}',
    'devid': '4931f7e6-d0fb-44ff-b0d3-6a252bacdccb',
    'pragma': 'no-cache',
    'referer': 'https://www.oklink.com/cn/btc/tx-list/large',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-apikey': key,
    'x-cdn': 'https://static.oklink.com',
    'x-locale': 'zh_CN',
    'x-utc': '8',
}

response = requests.get(
    'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict?t=1689944194516&offset=0&txType=&limit=20&sort=realTransferValue,desc',
    cookies=cookies,
    headers=headers,
).json()

print(response)
