# Erstellung einer Parsing-Hilfsfunktion

Erstellen Sie eine neue Datei `reader.py`. Definieren Sie in dieser Datei eine Hilfsfunktion `read_csv_as_dicts()`, die eine Datei mit CSV-Daten in eine Liste von Dictionaries liest, wobei der Benutzer die Typumwandlungen für jede Spalte angibt.

So soll es funktionieren:

```python
>>> import reader
>>> portfolio = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>> for s in portfolio:
         print(s)

{'name': 'AA','shares': 100, 'price': 32.2}
{'name': 'IBM','shares': 50, 'price': 91.1}
{'name': 'CAT','shares': 150, 'price': 83.44}
{'name': 'MSFT','shares': 200, 'price': 51.23}
{'name': 'GE','shares': 95, 'price': 40.37}
{'name': 'MSFT','shares': 50, 'price': 65.1}
{'name': 'IBM','shares': 100, 'price': 70.44}
>>>
```

Oder, wenn Sie die CTA-Daten lesen möchten:

```python
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [str,str,str,int])
>>> len(rows)
577563
>>> rows[0]
{'daytype': 'U', 'route': '3', 'rides': 7354, 'date': '01/01/2001'}
>>>
```
