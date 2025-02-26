# Bessere Ausgabe zur Darstellung von Objekten

Alle Python-Objekte haben zwei String-Darstellungen. Die erste Darstellung wird durch die String-Konvertierung via `str()` erstellt (die von `print` aufgerufen wird). Die String-Darstellung ist normalerweise eine gut formattierte Version des Objekts, die für Menschen gedacht ist. Die zweite Darstellung ist eine Code-Darstellung des Objekts, die durch `repr()` erstellt wird (oder einfach indem man einen Wert in der interaktiven Shell ansieht). Die Code-Darstellung zeigt Ihnen normalerweise den Code, den Sie eingeben müssen, um das Objekt zu erhalten. Hier ist ein Beispiel, das Datumsangaben veranschaulicht:

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # verwendet str()
2008-07-05
>>> d    # verwendet repr()
datetime.date(2008, 7, 5)
>>>
```

Es gibt mehrere Techniken, um die `repr()`-String in der Ausgabe zu erhalten:

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
>>>
```

Ändern Sie das von Ihnen erstellte `Stock`-Objekt so, dass die `__repr__()`-Methode eine nützlichere Ausgabe erzeugt. Beispielsweise:

```python
>>> goog = Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

Sehen Sie sich an, was passiert, wenn Sie ein Portfolio von Aktien lesen und die resultierende Liste ansehen, nachdem Sie diese Änderungen vorgenommen haben. Beispielsweise:

```python
>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23),
 Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
>>>
```
