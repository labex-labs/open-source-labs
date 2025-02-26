# Comment les programmes échouent

Python ne effectue aucune vérification ni validation des types ou des valeurs des arguments de fonction. Une fonction fonctionnera avec n'importe quel données compatible avec les instructions de la fonction.

```python
def add(x, y):
    return x + y

add(3, 4)               # 7
add('Hello', 'World')   # 'HelloWorld'
add('3', '4')           # '34'
```

Si des erreurs se produisent dans une fonction, elles apparaissent au moment de l'exécution (en tant qu'exception).

```python
def add(x, y):
    return x + y

>>> add(3, '4')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +:
'int' and 'str'
>>>
```

Pour vérifier le code, il y a une forte mise sur les tests (traité plus tard).
