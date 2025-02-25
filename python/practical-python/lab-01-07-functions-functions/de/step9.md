# Übung 1.32: Verwenden einer Bibliotheksfunktion

Python kommt mit einer großen Standardbibliothek von nützlichen Funktionen. Eine Bibliothek, die hier möglicherweise nützlich sein könnte, ist das `csv`-Modul. Sie sollten es verwenden, wenn Sie mit CSV-Datenfiles arbeiten müssen. Hier ist ein Beispiel, wie es funktioniert:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name','shares', 'price']
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>> f.close()
>>>
```

Ein schönes Merkmal des `csv`-Moduls ist, dass es sich um eine Vielzahl von niedrigen Details wie Anführungszeichen und richtiges Komma-Splitten kümmert. In der obigen Ausgabe werden Sie bemerken, dass es die Anführungszeichen von den Namen in der ersten Spalte entfernt hat.

Ändern Sie Ihr `pcost.py`-Programm so, dass es das `csv`-Modul für die Analyse verwendet, und versuchen Sie, frühere Beispiele auszuführen.
