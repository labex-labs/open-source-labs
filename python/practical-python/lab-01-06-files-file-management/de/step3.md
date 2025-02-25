# Übliche Muster zum Schreiben in eine Datei

String-Daten schreiben.

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
 ...
```

Die print-Funktion umleiten.

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
 ...
```

Diese Übungen basieren auf einer Datei `portfolio.csv`. Die Datei enthält eine Liste von Zeilen mit Informationen über ein Aktienportfolio. Es wird angenommen, dass Sie im Verzeichnis `~/project/` arbeiten. Wenn Sie sich nicht sicher sind, können Sie herausfinden, wo Python denkt, dass es läuft, indem Sie Folgendes tun:

```python
>>> import os
>>> os.getcwd()
'/home/labex/project' # Ausgabe variiert
>>>
```
