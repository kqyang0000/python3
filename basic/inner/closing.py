from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(str.line)
