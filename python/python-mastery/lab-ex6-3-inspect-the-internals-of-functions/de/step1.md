# Die Untersuchung von Funktionen

Definieren Sie eine einfache Funktion:

```python
>>> def add(x,y):
       'Adds two things'
       return x+y

>>>
```

Führen Sie `dir()` auf der Funktion aus, um ihre Attribute zu betrachten.

```python
>>> dir(add)
... betrachten Sie das Ergebnis...
>>>
```

Rufen Sie einige grundlegende Informationen wie den Funktionsnamen, den Namen des definierten Moduls und die Dokumentationszeichenfolge ab.

```python
>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>> add.__doc__
'Adds two things'
>>>
```

Das `__code__`-Attribut einer Funktion enthält tiefere Informationen über die Funktionsimplementierung. Überprüfen Sie, ob Sie dies betrachten können und die Anzahl der erforderlichen Argumente und die Namen der lokalen Variablen bestimmen können.
