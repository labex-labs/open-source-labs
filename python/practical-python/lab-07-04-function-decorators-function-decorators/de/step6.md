# Übung 7.10: Ein Dekorator zur Zeitmessung

Wenn Sie eine Funktion definieren, werden ihr Name und ihr Modul in den Attributen `__name__` und `__module__` gespeichert. Beispielsweise:

```python
>>> def add(x,y):
        return x+y

>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>>
```

In einer Datei `timethis.py` schreiben Sie einen Dekoratorfunktion `timethis(func)`, der eine Funktion mit einer zusätzlichen Logikschicht umschließt, die ausgibt, wie lange es für eine Funktion dauert, bis sie ausgeführt wird. Dazu umschließen Sie die Funktion mit Zeitmessaufrufen wie folgt:

```python
start = time.time()
r = func(*args,**kwargs)
end = time.time()
print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
```

Hier ist ein Beispiel dafür, wie Ihr Dekorator funktionieren sollte:

```python
>>> from timethis import timethis
>>> @timethis
def countdown(n):
    while n > 0:
        n -= 1

>>> countdown(10000000)
__main__.countdown : 0.076562
>>>
```

Diskussion: Dieser `@timethis`-Dekorator kann vor jeder Funktionsdefinition platziert werden. Somit können Sie ihn als diagnostisches Tool für die Leistungstuning verwenden.
