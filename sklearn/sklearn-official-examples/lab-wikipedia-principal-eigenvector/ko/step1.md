# 데이터 다운로드 (이미 디스크에 있는 경우 제외)

위키피디아 콘텐츠의 잠재 구조화된 데이터 추출인 DBpedia 덤프에서 데이터를 다운로드합니다.

```python
from bz2 import BZ2File
import os
from datetime import datetime
from urllib.request import urlopen

redirects_url = "http://downloads.dbpedia.org/3.5.1/en/redirects_en.nt.bz2"
redirects_filename = redirects_url.rsplit("/", 1)[1]

page_links_url = "http://downloads.dbpedia.org/3.5.1/en/page_links_en.nt.bz2"
page_links_filename = page_links_url.rsplit("/", 1)[1]

resources = [
    (redirects_url, redirects_filename),
    (page_links_url, page_links_filename),
]

for url, filename in resources:
    if not os.path.exists(filename):
        print("'%s'에서 데이터를 다운로드 중입니다. 잠시 기다려주십시오..." % url)
        opener = urlopen(url)
        with open(filename, "wb") as f:
            f.write(opener.read())
        print()
```
