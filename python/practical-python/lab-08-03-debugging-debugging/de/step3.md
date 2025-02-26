# Verwenden der interaktiven Python-Shell (REPL)

Verwenden Sie die Option `-i`, um Python bei der Ausführung eines Skripts am Leben zu halten.

```bash
$ python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", Zeile 13, in <module>
    foo()
  File "blah.py", Zeile 10, in foo
    bar()
  File "blah.py", Zeile 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' Objekt hat kein Attribut 'append'
>>>
```

Es bewahrt den Interpreter-Zustand auf. Das bedeutet, dass Sie nach dem Absturz herumstöbern können. Variable Werte und anderen Zustand prüfen.
