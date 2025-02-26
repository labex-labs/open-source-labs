# Ein Verarbeitungsleitungsaufbau

Ein großer Vorteil von Generatoren ist, dass sie es Ihnen ermöglichen, Programme zu erstellen, die Verarbeitungsleitungen aufbauen - ähnlich wie die Rohre auf Unix-Systemen. Experimentieren Sie mit diesem Konzept, indem Sie die folgenden Schritte ausführen:

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
        print(row)

['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Nun, das ist interessant. Was Sie hier sehen, ist, dass die Ausgabe der `follow()`-Funktion in die `csv.reader()`-Funktion geleitet wurde und wir jetzt eine Sequenz von aufgespaltenen Zeilen erhalten.
