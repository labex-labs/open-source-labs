# Änderung Ihrer Orientierung (in Spalten)

Sie können oft viel Arbeitsspeicher sparen, wenn Sie Ihre Sichtweise auf die Daten ändern. Beispielsweise, was passiert, wenn Sie alle Busdaten mithilfe dieser Funktion in Spalten einlesen?

```python
# readrides.py

...

def read_rides_as_columns(filename):
    '''
    Liest die Busfahrtdaten in 4 Listen ein, die Spalten repräsentieren
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Überspringt die Überschriften
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

Theoretisch sollte diese Funktion viel Arbeitsspeicher sparen. Lassen Sie uns es analysieren, bevor wir es testen.

Zunächst enthielt die Datendatei 577563 Zeilen mit Daten, wobei jede Zeile vier Werte enthielt. Wenn jede Zeile als Wörterbuch gespeichert wird, sind diese Wörterbücher minimal 240 Byte groß.

```python
>>> nrows = 577563     # Anzahl der Zeilen in der ursprünglichen Datei
>>> nrows * 240
138615120
>>>
```

Das sind also nur für die Wörterbücher selbst 138MB. Dies schließt keine der tatsächlich in den Wörterbüchern gespeicherten Werte ein.

Indem Sie zu Spalten wechseln, werden die Daten in 4 separate Listen gespeichert.\
Jede Liste erfordert 8 Byte pro Element, um einen Zeiger zu speichern. Hier ist also eine grobe Schätzung der Listenanforderungen:

```python
>>> nrows * 4 * 8
18482016
>>>
```

Das sind etwa 18MB an Listenüberhead. Wenn Sie also zu einer Spaltenorientierung wechseln, sollten Sie allein durch das Entfernen aller zusätzlichen Informationen, die in Wörterbüchern gespeichert werden müssen, etwa 120MB Arbeitsspeicher sparen.

Versuchen Sie, diese Funktion zu verwenden, um die Busdaten einzulesen und den Arbeitsspeicherbedarf zu betrachten.

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> columns = read_rides_as_columns('ctabus.csv')
>>> tracemalloc.get_traced_memory()
... schauen Sie sich das Ergebnis an...
>>>
```

Stimmt das Ergebnis mit den erwarteten Arbeitsspeichersparungen aus unseren obigen groben Berechnungen überein?
