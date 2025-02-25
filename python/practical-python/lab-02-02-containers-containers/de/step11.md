# Übung 2.6: Dictionaries als Container

Ein Dictionary ist eine nützliche Möglichkeit, um Elemente zu verfolgen, wenn Sie Elemente mithilfe eines Index anderen als einer ganzen Zahl aufrufen möchten. Versuchen Sie im Python-Shell, mit einem Dictionary zu experimentieren:

```python
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... schauen Sie sich das Ergebnis an...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... schauen Sie sich das Ergebnis an...
>>> 'AAPL' in prices
False
>>>
```

Die Datei `prices.csv` enthält eine Reihe von Zeilen mit Aktienpreisen. Die Datei sieht ungefähr so aus:

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

Schreiben Sie eine Funktion `read_prices(filename)`, die eine Reihe von Preisen wie diese in ein Dictionary liest, wobei die Schlüssel des Dictionaries die Aktiennamen sind und die Werte im Dictionary die Aktienpreise sind.

Um dies zu tun, beginnen Sie mit einem leeren Dictionary und fügen Sie Werte hinein, genauso wie Sie es oben getan haben. Allerdings lesen Sie die Werte jetzt aus einer Datei.

Wir werden diese Datenstruktur verwenden, um schnell den Preis eines angegebenen Aktiennamens zu suchen.

Einige kleine Tipps, die Sie für diesen Teil benötigen. Zunächst stellen Sie sicher, dass Sie das `csv`-Modul genauso verwenden wie zuvor - es ist hier nicht nötig, das Rad neu zu erfinden.

```python
>>> import csv
>>> f = open('/home/labex/project/prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['AA', '9.22']
['AXP', '24.85']
...
[]
>>>
```

Eine weitere kleine Komplikation ist, dass die Datei `prices.csv` möglicherweise einige leere Zeilen enthält. Beachten Sie, wie die letzte Zeile der obigen Daten eine leere Liste ist - was bedeutet, dass keine Daten auf dieser Zeile vorhanden waren.

Es besteht die Möglichkeit, dass dies zu einem Absturz Ihres Programms mit einer Ausnahme führt. Verwenden Sie die `try`- und `except`-Anweisungen, um dies entsprechend zu fangen. Gedanke: Würde es besser sein, mit einer `if`-Anweisung vor schlechten Daten zu schützen?

Sobald Sie Ihre `read_prices()`-Funktion geschrieben haben, testen Sie sie interaktiv, um sicherzustellen, dass sie funktioniert:

```python
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
>>>
```
