# Übung 3.15: `main()`-Funktionen

Fügen Sie in der Datei `report.py` eine `main()`-Funktion hinzu, die eine Liste von Befehlszeilenoptionen akzeptiert und die gleiche Ausgabe wie zuvor erzeugt. Sie sollten es interaktiv wie folgt ausführen können:

```python
>>> import report
>>> report.main(['/home/labex/project/report.py', '/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv'])
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

Ändern Sie die Datei `pcost.py` so, dass sie eine ähnliche `main()`-Funktion hat:

```python
>>> import pcost
>>> pcost.main(['/home/labex/project/pcost.py', '/home/labex/project/portfolio.csv'])
Total cost: 44671.15
>>>
```
