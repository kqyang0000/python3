import requests

r = requests.get('http://www.douban.com',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print('url:', r.url)
print('encoding:', r.encoding)
print('headers:', r.headers)
print('cookies:', r.cookies)
print('status_code:', r.status_code)
print('text:', r.text)
