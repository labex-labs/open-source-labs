# Télécharger les données, si elles ne sont pas déjà sur le disque

Nous allons télécharger les données à partir des dumps de DBpedia, qui est une extraction des données structurées latentes du contenu Wikipédia.

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
        print("Téléchargement des données depuis '%s', veuillez patienter..." % url)
        opener = urlopen(url)
        with open(filename, "wb") as f:
            f.write(opener.read())
        print()
```
