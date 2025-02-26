# Metadaten kopieren

Wenn eine Funktion von einem Dekorator umschlossen wird, verlierst du oft Informationen über den Namen der Funktion, die Dokumentationsstrings und andere Details. Überprüfe dies:

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function wrapper at 0x4439b0>
>>> help(add)
... schau dir die Ausgabe an...
>>>
```

Ändere die Definition des `logged`-Dekorators, sodass er die Funktionsmetadaten richtig kopiert. Dazu verwende den `@wraps(func)`-Dekorator wie in den Notizen gezeigt.

Nachdem du fertig bist, stell sicher, dass der Dekorator den Funktionsnamen und die Doc-String beibehält.

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function add at 0x4439b0>
>>> add.__doc__
'Adds two things'
>>>
```

Ändere den `@validated`-Dekorator, den du zuvor geschrieben hast, sodass er ebenfalls die Metadaten mit `@wraps(func)` beibehält.
