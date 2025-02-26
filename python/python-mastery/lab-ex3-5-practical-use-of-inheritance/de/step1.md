# Vorbereitung

Ein wichtiger Gebrauch von Klassen in Python besteht darin, Code zu schreiben, der auf verschiedene Weise erweitert/angepasst werden kann. Um dies zu veranschaulichen, haben Sie in Übung 3.2 eine Funktion `print_table()` erstellt, die Tabellen erstellt. Sie haben dies verwendet, um die Ausgabe aus der `portfolio`-Liste zu erzeugen. Beispielsweise:

```python
>>> import stock
>>> import reader
>>> import tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> tableformat.print_table(portfolio, ['name','shares','price'])
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Angenommen, Sie möchten, dass die Funktion `print_table()` Tabellen in einer beliebigen Anzahl von Ausgabeformaten wie CSV, XML, HTML, Excel usw. erstellen kann. Versuchen, die Funktion so zu modifizieren, dass sie alle diese Ausgabeformate gleichzeitig unterstützt, wäre schmerzhaft. Ein besseres Vorgehen hierfür besteht darin, den ausgaberelevanten Formatierungs-Code in eine Klasse zu verschieben und die Vererbung zu verwenden, um verschiedene Ausgabeformate zu implementieren.
