# Wiederholtes Erinnern

In den CTA-Bus-Daten haben wir festgestellt, dass es 181 eindeutige Buslinien gibt.

```python
>>> routes = { row['route'] for row in rows }
>>> len(routes)
181
>>>
```

Frage: Wie viele eindeutige Routenzeichenobjekte sind in den Fahrdaten enthalten? Anstatt eine Menge von Routen zu erstellen, erstellen Sie stattdessen eine Menge von Objekt-IDs:

```python
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
542305
>>>
```

Denken Sie sich das für einen Moment durch - es gibt nur 181 verschiedene Routennamen, aber die resultierende Liste von Dictionaries enthält 542305 verschiedene Routenzeichen. Vielleicht lässt sich das mit etwas Caching oder Objekt-Wiederverwendung beheben. Tatsächlich hat Python eine Funktion, die zum Cachen von Zeichenketten verwendet werden kann, `sys.intern()`. Beispielsweise:

```python
>>> a = 'hello world'
>>> b = 'hello world'
>>> a is b
False
>>> import sys
>>> a = sys.intern(a)
>>> b = sys.intern(b)
>>> a is b
True
>>>
```

Starten Sie Python neu und versuchen Sie Folgendes:

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, str, str, int])
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
181
>>>
````

Schauen Sie sich die Speichernutzung an.

```python
>>> tracemalloc.get_traced_memory()
... schauen Sie sich das Ergebnis an...
>>>
```

Der Speicher sollte erheblich sinken. Beobachtung: Es gibt auch eine Menge von Wiederholungen bei den Daten. Was passiert, wenn Sie auch die Datumszeichenketten cachen?

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, str, int])
>>> tracemalloc.get_traced_memory()
... schauen Sie sich das Ergebnis an...
>>>
````
