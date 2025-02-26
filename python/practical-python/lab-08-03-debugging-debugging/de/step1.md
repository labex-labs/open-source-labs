# Debugging-Tipps

Also, Ihr Programm ist abstürzt...

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
AttributeError: 'int' Objekt hat kein Attribut 'append'
```

Was tun jetzt?!
