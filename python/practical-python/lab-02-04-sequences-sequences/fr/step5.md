# Itération sur une séquence

La boucle `for` itère sur les éléments d'une séquence.

```python
>>> s = [1, 4, 9, 16]
>>> for i in s:
...     print(i)
...
1
4
9
16
>>>
```

À chaque itération de la boucle, vous obtenez un nouvel élément avec lequel travailler. Cette nouvelle valeur est placée dans la variable d'itération. Dans cet exemple, la variable d'itération est `x` :

```python
for x in s:         # `x` est une variable d'itération
  ...statements
```

À chaque itération, la valeur précédente de la variable d'itération est écrasée (le cas échéant). Après que la boucle ait fini, la variable conserve la dernière valeur.
