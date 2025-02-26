# Leyendo los informes de trazas

La última línea es la causa específica del error.

```bash
$ python3 blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
# Cause of the crash
AttributeError: 'int' object has no attribute 'append'
```

Sin embargo, no siempre es fácil de leer o entender.

_CONSEJO EXPERTO: Pega todo el informe de trazas en Google._
