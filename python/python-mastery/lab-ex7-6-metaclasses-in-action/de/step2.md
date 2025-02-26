# Staunen Sie erstaunt

Versuchen Sie, Ihre `teststock.py`-Einhheits-Tests über diese neue Datei auszuführen. Die meisten von ihnen sollten jetzt bestanden werden. Aus Spaß können Sie Ihre `Stock`-Klasse mit einigen der früheren Codeausschnitte für die Tabellenformatierung und das Lesen von Daten testen. Alles sollte funktionieren.

```python
>>> from stock import Stock
>>> from reader import read_csv_as_instances
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
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

Wundern Sie sich erneut über die endgültige `stock.py`-Datei und beobachten Sie, wie sauber der Code aussieht. Versuchen Sie einfach nicht, an alles zu denken, was im Hintergrund mit der `Structure`-Basis-Klasse passiert.
