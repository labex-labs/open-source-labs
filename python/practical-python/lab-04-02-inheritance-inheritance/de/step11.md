# Mehrfachvererbung

Du kannst von mehreren Klassen erben, indem du sie in der Klassendefinition angibst.

```python
class Mother:
...

class Father:
...

class Child(Mother, Father):
...
```

Die Klasse `Child` erbt Eigenschaften von beiden Elternklassen. Es gibt einige recht knifflige Details. Mach es nicht, es sei denn, du weißt, was du tust. In der nächsten Abschnitt werden einige weitere Informationen gegeben, aber wir werden in diesem Kurs nicht weiter auf Mehrfachvererbung zurückgreifen.

Ein wichtiger Einsatz von Vererbung besteht darin, Code zu schreiben, der auf verschiedene Weise erweitert oder angepasst werden soll - insbesondere in Bibliotheken oder Frameworks. Um dies zu veranschaulichen, betrachte die Funktion `print_report()` in deinem Programm `report.py`. Sie sollte ungefähr so aussehen:

```python
def print_report(reportdata):
    '''
    Druckt eine schön formattierte Tabelle aus einer Liste von (Name, Anteile, Preis, Änderung) - Tupeln.
    '''
    headers = ('Name','Anteile','Preis','Änderung')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 +' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
```

Wenn du dein Report-Programm ausführst, solltest du eine Ausgabe wie diese erhalten:

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
```
