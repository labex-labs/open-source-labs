# Descarregar dados, se ainda não estiverem no disco

Descarregaremos os dados dos dumps do DBpedia, que é uma extração dos dados estruturados latentes do conteúdo da Wikipédia.

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
        print("A descarregar dados de '%s', aguarde..." % url)
        opener = urlopen(url)
        with open(filename, "wb") as f:
            f.write(opener.read())
        print()
```
