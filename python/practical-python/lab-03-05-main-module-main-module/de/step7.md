# Befehlszeilenargumente

Die Befehlszeile ist eine Liste von Textzeichenketten.

```bash
$ python3 report.py portfolio.csv prices.csv
```

Diese Liste von Textzeichenketten wird in `sys.argv` gefunden.

```python
# In der vorherigen bash-Anweisung
sys.argv # ['report.py, 'portfolio.csv', 'prices.csv']
```

Hier ist ein einfaches Beispiel zur Verarbeitung der Argumente:

```python
import sys

if len(sys.argv)!= 3:
    raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
portfile = sys.argv[1]
pricefile = sys.argv[2]
...
```
