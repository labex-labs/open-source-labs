# Tracebacks lesen

Die letzte Zeile ist die spezifische Ursache des Absturzes.

```bash
$ python3 blah.py
Traceback (most recent call last):
  File "blah.py", Zeile 13, in <module>
    foo()
  File "blah.py", Zeile 10, in foo
    bar()
  File "blah.py", Zeile 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
# Ursache des Absturzes
AttributeError: 'int' Objekt hat kein Attribut 'append'
```

Es ist jedoch nicht immer einfach, sie zu lesen oder zu verstehen.

_PRO-TIPP: Fügen Sie den gesamten Traceback in Google ein._
