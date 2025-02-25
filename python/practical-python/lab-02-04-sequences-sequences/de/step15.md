# Übung 2.16: Verwendung der zip()-Funktion

In der Datei `portfolio.csv` enthält die erste Zeile die Spaltenüberschriften. In all unserem bisherigen Code haben wir sie ignoriert.

```python
>>> f = open('/home/labex/project/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name','shares', 'price']
>>>
```

Was passiert aber, wenn Sie die Überschriften für etwas Nützliches verwenden könnten? Hier kommt die `zip()`-Funktion ins Spiel. Versuchen Sie zuerst, die Dateiüberschriften mit einer Datenzeile zu verknüpfen:

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

Bemerken Sie, wie `zip()` die Spaltenüberschriften mit den Spaltenwerten verknüpft. Wir haben hier `list()` verwendet, um das Ergebnis in eine Liste zu verwandeln, damit Sie es sehen können. Normalerweise erstellt `zip()` einen Iterator, der von einer `for`-Schleife verarbeitet werden muss.

Diese Verknüpfung ist ein Zwischenschritt bei der Erstellung eines Wörterbuchs. Versuchen Sie jetzt das Folgende:

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

Diese Transformation ist eine der nützlichsten Tricks, die Sie kennen sollten, wenn Sie mit vielen Datenfiles arbeiten. Beispielsweise nehmen Sie an, Sie möchten das `pcost.py`-Programm so ändern, dass es mit verschiedenen Eingabedateien funktioniert, ohne auf die tatsächliche Spaltennummer zu achten, in der der Name, die Anzahl der Anteile und der Preis erscheinen.

Ändern Sie die `portfolio_cost()`-Funktion in `pcost.py` so, dass sie wie folgt aussieht:

```python
# pcost.py

def portfolio_cost(filename):
 ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # Dies fängt Fehler bei der Umwandlung in int() und float() oben ab
            except ValueError:
                print(f'Zeile {rowno}: Schlechte Zeile: {row}')
 ...
```

Versuchen Sie jetzt Ihre Funktion auf eine völlig andere Datenfile `portfoliodate.csv`, die wie folgt aussieht:

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('/home/labex/project/portfoliodate.csv')
44671.15
>>>
```

Wenn Sie es richtig gemacht haben, werden Sie feststellen, dass Ihr Programm weiterhin funktioniert, auch wenn die Datenfile ein völlig anderer Spaltenformat als zuvor hat. Das ist cool!

Die hier vorgenommene Änderung ist subtil, aber signifikant. Anstatt dass `portfolio_cost()` hartcodiert ist, um eine einzelne feste Dateiformat zu lesen, liest die neue Version jede CSV-Datei und extrahiert die interessanten Werte daraus. Solange die Datei die erforderlichen Spalten hat, wird der Code funktionieren.

Ändern Sie das `report.py`-Programm, das Sie in Abschnitt 2.3 geschrieben haben, so, dass es die gleiche Technik verwendet, um die Spaltenüberschriften auszuwählen.

Versuchen Sie, das `report.py`-Programm auf der `portfoliodate.csv`-Datei auszuführen und sehen Sie, dass es die gleiche Antwort wie zuvor liefert.
