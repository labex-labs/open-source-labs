# Verwendung der Funktionen `enumerate()` und `zip()`

In diesem Schritt werden wir zwei äußerst nützliche eingebaute Funktionen in Python erkunden, die für die Iteration unerlässlich sind: `enumerate()` und `zip()`. Diese Funktionen können Ihren Code erheblich vereinfachen, wenn Sie mit Sequenzen arbeiten.

## Zählen mit `enumerate()`

Wenn Sie über eine Sequenz iterieren, müssen Sie oft den Index oder die Position jedes Elements verfolgen. Hier kommt die `enumerate()`-Funktion ins Spiel. Die `enumerate()`-Funktion nimmt eine Sequenz als Eingabe und gibt für jedes Element in dieser Sequenz Paare aus (Index, Wert) zurück.

Wenn Sie im Python-Interpreter aus dem vorherigen Schritt weitergefahren sind, können Sie ihn weiterhin verwenden. Wenn nicht, starten Sie eine neue Sitzung. Hier ist, wie Sie die Daten einrichten können, wenn Sie neu beginnen:

```python
# If you're starting a new session, reload the data first:
# import csv
# f = open('portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# Use enumerate to get row numbers
for rowno, row in enumerate(rows):
    print(rowno, row)
```

Wenn Sie den obigen Code ausführen, erzeugt die `enumerate(rows)`-Funktion Paare aus einem Index (beginnend bei 0) und der entsprechenden Zeile aus der `rows`-Sequenz. Die `for`-Schleife entpackt dann diese Paare in die Variablen `rowno` und `row`, und wir geben sie aus.

Ausgabe:

```
0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
```

Wir können den Code noch lesbarer gestalten, indem wir `enumerate()` mit Entpackung kombinieren. Die Entpackung ermöglicht es uns, die Elemente einer Sequenz direkt einzelnen Variablen zuzuweisen.

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

In diesem Code verwenden wir ein zusätzliches Klammerpaar um `(name, shares, price)`, um die Zeilendaten richtig zu entpacken. Die `enumerate(rows)`-Funktion gibt uns immer noch den Index und die Zeile, aber jetzt entpacken wir die Zeile in die Variablen `name`, `shares` und `price`.

Ausgabe:

```
0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
```

## Paarung von Daten mit `zip()`

Die `zip()`-Funktion ist ein weiteres leistungsstarkes Werkzeug in Python. Sie wird verwendet, um entsprechende Elemente aus mehreren Sequenzen zu kombinieren. Wenn Sie mehrere Sequenzen an `zip()` übergeben, erstellt es einen Iterator, der Tupel erzeugt, wobei jedes Tupel Elemente aus jeder der Eingabesequenzen an der gleichen Position enthält.

Schauen wir uns an, wie wir `zip()` mit den `headers`- und `row`-Daten verwenden können, mit denen wir gearbeitet haben.

```python
# Recall the headers variable from earlier
print(headers)  # Should show ['name', 'shares', 'price']

# Get the first row
row = rows[0]
print(row)      # Should show ['AA', '100', '32.20']

# Use zip to pair column names with values
for col, val in zip(headers, row):
    print(col, val)
```

In diesem Code nimmt `zip(headers, row)` die `headers`-Sequenz und die `row`-Sequenz und paart ihre entsprechenden Elemente. Die `for`-Schleife entpackt dann diese Paare in `col` (für den Spaltennamen aus `headers`) und `val` (für den Wert aus `row`), und wir geben sie aus.

Ausgabe:

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

Eine sehr häufige Verwendung von `zip()` besteht darin, Wörterbücher aus Schlüssel-Wert-Paaren zu erstellen. In Python ist ein Wörterbuch eine Sammlung von Schlüssel-Wert-Paaren.

```python
# Create a dictionary from headers and row values
record = dict(zip(headers, row))
print(record)
```

Hier erstellt `zip(headers, row)` Paare aus Spaltennamen und Werten, und die `dict()`-Funktion nimmt diese Paare und wandelt sie in ein Wörterbuch um.

Ausgabe:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

Wir können diese Idee erweitern, um alle Zeilen in unserer `rows`-Sequenz in Wörterbücher umzuwandeln.

```python
# Convert all rows to dictionaries
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

In dieser Schleife verwenden wir für jede Zeile in `rows` `zip(headers, row)`, um Schlüssel-Wert-Paare zu erstellen, und dann `dict()`, um diese Paare in ein Wörterbuch umzuwandeln. Diese Technik ist in Datenverarbeitungsanwendungen sehr verbreitet, insbesondere wenn Sie mit CSV-Dateien arbeiten, bei denen die erste Zeile die Überschriften enthält.

Ausgabe:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
```
