# Schnittstellen und Typüberprüfung

Ändern Sie die Funktion `print_table()`, so dass sie überprüft, ob die übergebene Formatter-Instanz von `TableFormatter` erbt. Wenn nicht, werfen Sie einen `TypeError`.

Ihr neuer Code sollte Situationen wie diese erkennen:

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass

>>> tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())
Traceback (most recent call last):
...
TypeError: Expected a TableFormatter
>>>
```

Das Hinzufügen einer solchen Prüfung kann das Programm gewissermaßen sicherer machen. Denken Sie jedoch daran, dass die Typüberprüfung in Python ziemlich schwach ist. Es ist nicht garantiert, dass das Objekt, das als Formatter übergeben wird, auch dann richtig funktioniert, wenn es zufällig von der richtigen Basisklasse erbt. Der nächste Teil behandelt dieses Problem.
