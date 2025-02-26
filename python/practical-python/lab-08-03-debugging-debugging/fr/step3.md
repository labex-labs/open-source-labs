# Utilisation de la console interactive Python (REPL)

Utilisez l'option `-i` pour maintenir Python actif lors de l'exécution d'un script.

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

Elle conserve l'état de l'interpréteur. Cela signifie que vous pouvez examiner le code après le crash. Vérifier les valeurs des variables et d'autres états.
