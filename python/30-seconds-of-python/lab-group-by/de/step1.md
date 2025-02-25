# Listelemente gruppieren

Schreiben Sie eine Funktion `group_by(lst, fn)`, die eine Liste `lst` und eine Funktion `fn` als Argumente nimmt und ein Dictionary zurückgibt, wobei die Schlüssel die Ergebnisse der Anwendung von `fn` auf die Elemente von `lst` sind und die Werte Listen von Elementen aus `lst` sind, die den entsprechenden Schlüssel erzeugen, wenn `fn` auf sie angewendet wird.

Wenn wir beispielsweise eine Liste von Zahlen `[6.1, 4.2, 6.3]` haben und sie nach ihrem ganzzahligen Teil gruppieren möchten, können wir die `floor`-Funktion aus dem `math`-Modul als Gruppierungsfunktion verwenden. Die erwartete Ausgabe wäre `{4: [4.2], 6: [6.1, 6.3]}`.

```python
from collections import defaultdict

def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
```

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```
