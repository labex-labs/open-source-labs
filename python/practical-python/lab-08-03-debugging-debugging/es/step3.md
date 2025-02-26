# Usando la REPL

Utiliza la opción `-i` para mantener Python activo al ejecutar un script.

```bash
$ python3 -i blah.py
Traceback (most recent call last):
  File "blah.py", line 13, in?
    foo()
  File "blah.py", line 10, in foo
    bar()
  File "blah.py", line 7, in bar
    spam()
  File "blah.py", 4, in spam
    line x.append(3)
AttributeError: 'int' object has no attribute 'append'
>>>
```

Preserva el estado del intérprete. Eso significa que puedes investigar después del error. Verificar los valores de las variables y otros estados.
