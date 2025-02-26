# Votre premier décorateur avec des arguments

Le décorateur `@logged` que vous avez défini précédemment affiche toujours un message simple avec le nom de la fonction. Supposons que vous vouliez que l'utilisateur puisse spécifier un message personnalisé de quelque sorte.

Définissez un nouveau décorateur `@logformat(fmt)` qui accepte une chaîne de formatage en tant qu'argument et utilise `fmt.format(func=func)` pour formater une fonction fournie en un message de journalisation :

```python
# sample.py
...
from logcall import logformat

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x,y):
    return x*y
```

Pour ce faire, vous devez définir un décorateur qui prend un argument. Voici à quoi cela devrait ressembler lorsque vous le testez :

```python
>>> import sample
Adding logging to add
Adding logging to sub
Adding logging to mul
>>> sample.add(2,3)
Appel de add
5
>>> sample.mul(2,3)
sample.py:mul
6
>>>
```

Pour simplifier encore le code, montrez comment vous pouvez définir le décorateur original `@logged` à l'aide du décorateur `@logformat`.
