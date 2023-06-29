import requests

p = {
    'wd': 'python'
}

r = requests.get('http://httpbin.org/get', params=p)
r.encoding = 'utf-8'

print(r.text)