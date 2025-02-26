# Übung 3.17: Von Dateinamen zu dateilichen Objekten

Sie haben jetzt eine Datei `fileparse.py` erstellt, die eine Funktion `parse_csv()` enthielt. Die Funktion funktionierte wie folgt:

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>>
```

Derzeit erwartet die Funktion, dass ihr ein Dateiname übergeben wird. Sie können den Code jedoch flexibler gestalten. Ändern Sie die Funktion so, dass sie mit jedem dateilichen/iterierbaren Objekt funktioniert. Beispielsweise:

```python
>>> import fileparse
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

In diesem neuen Code passiert, wenn Sie wie zuvor einen Dateinamen übergeben?

```python
>>> port = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>> port
... schauen Sie sich die Ausgabe an (es sollte etwas verrückt sein)...
>>>
```

Ja, Sie müssen vorsichtig sein. Können Sie eine Sicherheitsüberprüfung hinzufügen, um dies zu vermeiden?
