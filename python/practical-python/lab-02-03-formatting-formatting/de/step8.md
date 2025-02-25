# Übung 2.10: Ausgabe einer formatierten Tabelle

Wiederholen Sie die for-Schleife in Übung 2.9, aber ändern Sie den print-Befehl, um die Tupel zu formatieren.

```python
>>> for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

Sie können auch die Werte erweitern und f-Strings verwenden. Beispielsweise:

```python
>>> for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

Nehmen Sie die obigen Anweisungen und fügen Sie sie Ihrem `report.py`-Programm hinzu. Lassen Sie Ihr Programm die Ausgabe der `make_report()`-Funktion entgegennehmen und geben Sie eine schön formatierte Tabelle wie gezeigt aus.
