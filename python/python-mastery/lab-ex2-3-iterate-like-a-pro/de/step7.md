# Ein spürbarer Speicherersparnis

In Übung 2.1 haben Sie eine Funktion `read_rides_as_dicts()` geschrieben, die die CTA-Busdaten in eine Liste von Dictionaries einliest. Die Verwendung davon erfordert viel Speicher. Beispielsweise suchen wir den Tag, an dem der Buslinie 22 die höchste Fahrgastzahl hatte:

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rt22 = [row for row in rows if row['route'] == '22']
>>> max(rt22, key=lambda row: row['rides'])
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... schauen Sie sich das Ergebnis an. Sollte ungefähr 220MB betragen
>>>
```

Nun probieren wir ein Beispiel mit Generatoren. Neustarten Sie Python und versuchen Sie dies:

```python
>>> # NEUSTART
>>> import tracemalloc
>>> tracemalloc.start()
>>> import csv
>>> f = open('ctabus.csv')
>>> f_csv = csv.reader(f)
>>> headers = next(f_csv)
>>> rows = (dict(zip(headers,row)) for row in f_csv)
>>> rt22 = (row for row in rows if row['route'] == '22')
>>> max(rt22, key=lambda row: int(row['rides']))
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... schauen Sie sich das Ergebnis an. Sollte viel kleiner als zuvor sein
>>>
```

Denken Sie daran, dass Sie das gesamte Datensatz behandelt haben, als wäre er als eine Sequenz von Dictionaries gespeichert. Dennoch haben Sie nirgends tatsächlich eine Liste von Dictionaries erstellt und gespeichert. Nicht alle Probleme können auf diese Weise strukturiert werden, aber wenn Sie mit Daten iterativ arbeiten können, können Generator-Ausdrücke einen enormen Speicherersparnis bringen.
