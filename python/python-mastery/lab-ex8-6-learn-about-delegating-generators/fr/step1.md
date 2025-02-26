# Exemple : Réception de messages

Dans l'exercice 8.3, nous avons examiné les définitions de coroutines. Les coroutines étaient des fonctions auxquelles vous envoyiez des données. Par exemple :

```python
>>> from cofollow import consumer
>>> @consumer
    def printer():
        while True:
            item = yield
            print('Got:', item)

>>> p = printer()
>>> p.send('Hello')
Got: Hello
>>> p.send('World')
Got: World
>>>
```

À l'époque, il aurait peut-être été intéressant d'utiliser `yield` pour recevoir une valeur. Cependant, si vous regardez vraiment le code, il semble assez étrange - un simple `yield` comme ça? Qu'est-ce qui se passe là?

Dans le fichier `cofollow.py`, définissez la fonction suivante :

```python
def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg
```

Cette fonction reçoit un message, puis vérifie qu'il est du type attendu. Essayez :

```python
>>> from cofollow import consumer, receive
>>> @consumer
    def print_ints():
        while True:
             val = yield from receive(int)
             print('Got:', val)

>>> p = print_ints()
>>> p.send(42)
Got: 42
>>> p.send(13)
Got: 13
>>> p.send('13')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
...
AssertionError: Expected type <class 'int'>
>>>
```

Du point de vue de la lisibilité, l'instruction `yield from receive(int)` est un peu plus descriptive - elle indique que la fonction va attendre jusqu'à recevoir un message d'un type donné.

Maintenant, modifiez toutes les coroutines dans `coticker.py` pour utiliser la nouvelle fonction `receive()` et assurez-vous que le code de l'exercice 8.3 fonctionne toujours.
