# Ihr erster Dekorator

Um mit Dekoratoren zu beginnen, schreiben Sie eine _sehr_ einfache Dekoratorfunktion, die einfach eine Nachricht ausgibt, wenn eine Funktion aufgerufen wird. Erstellen Sie eine Datei `logcall.py` und definieren Sie die folgende Funktion:

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Erstellen Sie nun eine separate Datei `sample.py` und wenden Sie sie auf einige Funktionsdefinitionen an:

```python
# sample.py

from logcall import logged

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y
```

Testen Sie Ihren Code wie folgt:

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3,4)
Calling add
7
>>> sample.sub(2,3)
Calling sub
-1
>>>
```
