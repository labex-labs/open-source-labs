# Lèvement d'exceptions

Dans le fichier `cofollow.py`, vous avez créé une coroutine `printer()`. Modifiez le code pour attraper et signaler les exceptions comme ceci :

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
            print('ERREUR : %r' % e)
```

Maintenant, essayez une expérience :

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')
hello
>>> p.send(42)
42
>>> p.throw(ValueError('It failed'))
ERREUR : ValueError('It failed',)
>>> try:
        int('n/a')
    except ValueError as e:
        p.throw(e)

ERREUR : ValueError("invalid literal for int() with base 10: 'n/a'",)
>>>
```

Remarquez comment le générateur en cours d'exécution n'est pas terminé par l'exception. Cela permet simplement à l'instruction `yield` de signaler une erreur au lieu de recevoir une valeur.
