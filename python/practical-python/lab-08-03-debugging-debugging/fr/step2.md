# Lecture des traces d'erreur

La dernière ligne est la cause spécifique du crash.

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

Cependant, il n'est pas toujours facile de lire ou de comprendre.

_POINT D'ASTUCE : Collez toute la trace d'erreur dans Google._
