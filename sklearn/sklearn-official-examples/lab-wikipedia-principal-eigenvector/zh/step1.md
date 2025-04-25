# 若数据不在本地磁盘，则下载数据

我们将从 DBpedia 转储中下载数据，该转储是维基百科内容的潜在结构化数据的提取。

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
        print("Downloading data from '%s', please wait..." % url)
        opener = urlopen(url)
        with open(filename, "wb") as f:
            f.write(opener.read())
        print()
```
