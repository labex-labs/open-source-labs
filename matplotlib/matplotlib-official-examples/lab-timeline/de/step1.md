# Daten abrufen

Um eine Zeitlinie zu erstellen, müssen wir Daten wie Datum und Name abrufen. In diesem Beispiel verwenden wir die Veröffentlichungen von Matplotlib und deren Daten von GitHub. Wenn die Daten aus irgendeinem Grund nicht abgerufen werden können, verwenden wir als Backup die Fallback-Daten. Hier ist der Code zum Abrufen der Daten:

```python
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.dates as mdates

try:
    # Versuche, eine Liste der Matplotlib-Veröffentlichungen und deren Daten
    # von https://api.github.com/repos/matplotlib/matplotlib/releases abzurufen
    import json
    import urllib.request

    url = 'https://api.github.com/repos/matplotlib/matplotlib/releases'
    url += '?per_page=100'
    data = json.loads(urllib.request.urlopen(url, timeout=1).read().decode())

    dates = []
    names = []
    for item in data:
        if 'rc' not in item['tag_name'] and 'b' not in item['tag_name']:
            dates.append(item['published_at'].split("T")[0])
            names.append(item['tag_name'])
    # Konvertiere Datumsstrings (z.B. 2014-10-18) in datetime
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

except Exception:
    # Wenn das obige fehlschlägt, z.B. aufgrund eines fehlenden Internetverbindungs
    # verwende die folgenden Listen als Fallback.
    names = ['v2.2.4', 'v3.0.3', 'v3.0.2', 'v3.0.1', 'v3.0.0', 'v2.2.3',
             'v2.2.2', 'v2.2.1', 'v2.2.0', 'v2.1.2', 'v2.1.1', 'v2.1.0',
             'v2.0.2', 'v2.0.1', 'v2.0.0', 'v1.5.3', 'v1.5.2', 'v1.5.1',
             'v1.5.0', 'v1.4.3', 'v1.4.2', 'v1.4.1', 'v1.4.0']

    dates = ['2019-02-26', '2019-02-26', '2018-11-10', '2018-11-10',
             '2018-09-18', '2018-08-10', '2018-03-17', '2018-03-16',
             '2018-03-06', '2018-01-18', '2017-12-10', '2017-10-07',
             '2017-05-10', '2017-05-02', '2017-01-17', '2016-09-09',
             '2016-07-03', '2016-01-10', '2015-10-29', '2015-02-16',
             '2014-10-26', '2014-10-18', '2014-08-26']

    # Konvertiere Datumsstrings (z.B. 2014-10-18) in datetime
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
```
