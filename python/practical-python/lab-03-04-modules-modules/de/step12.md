# Übung 3.11: Modulimporte

Im Abschnitt 3 haben wir eine allgemein nutzbare Funktion `parse_csv()` erstellt, um die Inhalte von CSV-Datendateien zu analysieren.

Jetzt werden wir sehen, wie man diese Funktion in anderen Programmen verwenden kann. Beginnen Sie zunächst in einem neuen Shell-Fenster. Navigieren Sie zum Ordner, in dem Sie alle Ihre Dateien haben. Wir werden sie importieren.

Starten Sie die interaktive Python-Betriebsmode.

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Sobald Sie das getan haben, versuchen Sie, einige der zuvor geschriebenen Programme zu importieren. Sie sollten genauso wie zuvor deren Ausgabe sehen. Um zu betonen: Beim Importieren eines Moduls wird dessen Code ausgeführt.

```python
>>> import bounce
... Ausgabe anzeigen...
>>> import mortgage
... Ausgabe anzeigen...
>>> import report
... Ausgabe anzeigen...
>>>
```

Wenn nichts davon funktioniert, laufen Sie wahrscheinlich Python im falschen Verzeichnis. Versuchen Sie jetzt, Ihr `fileparse`-Modul zu importieren und Hilfe zu erhalten.

```python
>>> import fileparse
>>> help(fileparse)
... Ausgabe ansehen...
>>> dir(fileparse)
... Ausgabe ansehen...
>>>
```

Versuchen Sie, das Modul zum Lesen einiger Daten zu verwenden:

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... Ausgabe ansehen...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... Ausgabe ansehen...
>>> prices = dict(pricelist)
>>> prices
... Ausgabe ansehen...
>>> prices['IBM']
106.28
>>>
```

Versuchen Sie, eine Funktion zu importieren, so dass Sie den Modulnamen nicht mehr angeben müssen:

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... Ausgabe ansehen...
>>>
```
