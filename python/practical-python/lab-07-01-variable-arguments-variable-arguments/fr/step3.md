# Combiner les deux

Une fonction peut également accepter un nombre quelconque d'arguments variables de mot clé et d'arguments non de mot clé.

```python
def f(*args, **kwargs):
...
```

Appel de fonction.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

Les arguments sont séparés en composants positionnels et de mot clé

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
  ...
```

Cette fonction prend toute combinaison d'arguments positionnels ou de mot clé. Elle est parfois utilisée lorsqu'on écrit des wrappers ou lorsqu'on veut passer des arguments à une autre fonction.
