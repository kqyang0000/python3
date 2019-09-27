import chardet

de = chardet.detect(b'Hello World')
print(de)
data = '中文'.encode('utf-8')
de = chardet.detect(data)
print(de)
