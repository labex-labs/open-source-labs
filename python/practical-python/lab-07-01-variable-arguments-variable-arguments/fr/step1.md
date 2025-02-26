# Arguments variables positionnels (\*args)

Une fonction qui accepte _n'importe quel nombre_ d'arguments est dite utiliser des arguments variables. Par exemple :

```python
def f(x, *args):
  ...
```

Appel de fonction.

```python
f(1,2,3,4,5)
```

Les arguments supplémentaires sont passés sous forme de tuple.

```python
def f(x, *args):
    # x -> 1
    # args -> (2,3,4,5)
```
