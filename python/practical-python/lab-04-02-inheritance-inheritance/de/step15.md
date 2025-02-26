# Übung 4.8: Alles zusammenbringen

Ändern Sie das Programm `report.py` so, dass die Funktion `portfolio_report()` ein optionales Argument erhält, das das Ausgabeformat angibt. Beispielsweise:

```python
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'txt')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

Ändern Sie das Hauptprogramm so, dass ein Format über die Befehlszeile angegeben werden kann:

```bash
$ python3 report.py portfolio.csv prices.csv csv
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
$
```
