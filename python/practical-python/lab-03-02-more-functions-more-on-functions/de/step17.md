# Übung 3.7: Auswählen eines anderen Spaltentrennzeichens

Obwohl CSV-Dateien ziemlich üblich sind, ist es auch möglich, dass Sie eine Datei finden, die ein anderes Spaltentrennzeichen wie ein Tabulator oder ein Leerzeichen verwendet. Beispielsweise sieht die Datei `portfolio.dat` so aus:

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

Die `csv.reader()`-Funktion erlaubt, ein anderes Spaltentrennzeichen anzugeben, wie folgt:

```python
rows = csv.reader(f, delimiter=' ')
```

Ändern Sie Ihre `parse_csv()`-Funktion im Verzeichnis `/home/labex/project/fileparse_3.7.py` so, dass sie auch das Spaltentrennzeichen ändern lässt.

Beispielsweise:

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23}, {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```
