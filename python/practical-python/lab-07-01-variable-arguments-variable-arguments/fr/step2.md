# Arguments variables de mot clé (\*\*kwargs)

Une fonction peut également accepter un nombre quelconque d'arguments de mot clé. Par exemple :

```python
def f(x, y, **kwargs):
 ...
```

Appel de fonction.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

Les mots clés supplémentaires sont passés dans un dictionnaire.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
```
