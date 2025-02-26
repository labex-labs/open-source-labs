# Code qui effectue la journalisation

Peut-être que vous pouvez créer une fonction qui ajoute la journalisation à d'autres fonctions. Un wrapper.

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Appel de', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Maintenant, utilisez-la.

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

Que se passe-t-il lorsque vous appelez la fonction renvoyée par `logged`?

```python
logged_add(3, 4)      # Vous voyez le message de journalisation apparaître
```

Cet exemple illustre le processus de création d'une fonction dite _wrapper_.

Un wrapper est une fonction qui s'enveloppe autour d'une autre fonction avec quelques traitements supplémentaires, mais qui fonctionne exactement de la même manière que la fonction d'origine.

```python
>>> logged_add(3, 4)
Appel de add   # Sortie supplémentaire. Ajoutée par le wrapper
7
>>>
```

_Nota : La fonction `logged()` crée le wrapper et le renvoie en résultat._
