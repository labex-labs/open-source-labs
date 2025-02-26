# Im Bus festgefahren

Die Datei `ctabus.csv` ist eine CSV-Datei, die tägliche Fahrgastzahlen für das Busssystem der Chicago Transit Authority (CTA) vom 1. Januar 2001 bis 31. August 2013 enthält. Sie enthält ungefähr 577.000 Zeilen an Daten. Verwenden Sie Python, um ein paar Zeilen der Daten anzuzeigen, um zu sehen, wie sie aussehen:

```python
>>> f = open('/home/labex/project/ctabus.csv')
>>> next(f)
'route,date,daytype,rides\n'
>>> next(f)
'3,01/01/2001,U,7354\n'
>>> next(f)
'4,01/01/2001,U,9288\n'
>>>
```

Es gibt 4 Spalten an Daten.

- route: Spalte 0. Der Name der Buslinie.
- date: Spalte 1. Ein Datumsstring im Format MM/DD/YYYY.
- daytype: Spalte 2. Ein Tagstyp-Code (U=Sonntag/Festtag, A=Samstag, W=Werktag)
- rides: Spalte 3. Gesamtzahl der Fahrgäste (ganzzahlig)

Die Spalte `rides` enthält die Gesamtzahl der Personen, die an einem bestimmten Tag in einer bestimmten Linie eingestiegen sind. Also, aus dem Beispiel, 7354 Personen sind am 1. Januar 2001 in der Linie 3 gefahren.
