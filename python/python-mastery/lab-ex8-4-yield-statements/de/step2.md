# Ausnahmen auslösen

In der Datei `cofollow.py` haben Sie einen Coroutin `printer()` erstellt. Ändern Sie den Code, um Ausnahmen zu fangen und zu melden, wie folgt:

```python
# cofollow.py
...
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('FEHLER: %r' % e)
```

Jetzt führen Sie ein Experiment durch:

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')
hello
>>> p.send(42)
42
>>> p.throw(ValueError('Es ist fehlgeschlagen'))
FEHLER: ValueError('Es ist fehlgeschlagen',)
>>> versuche:
        int('n/a')
    except ValueError als e:
        p.throw(e)

FEHLER: ValueError("ungültiger Literal für int() mit Basis 10: 'n/a'",)
>>>
```

Bemerken Sie, wie der laufende Generator nicht durch die Ausnahme beendet wird. Dies erlaubt lediglich, dass die `yield`-Anweisung einen Fehler signalisiert, anstatt einen Wert zu empfangen.
