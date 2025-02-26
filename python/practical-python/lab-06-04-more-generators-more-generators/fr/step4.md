# Exercice 6.13 : Expressions de générateur

Les expressions de générateur sont une version génératrice d'une compréhension de liste. Par exemple :

```python
>>> nums = [1, 2, 3, 4, 5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x109207e60>
>>> for n in squares:
...     print(n)
...
1
4
9
16
25
```

Contrairement à une compréhension de liste, une expression de générateur ne peut être utilisée qu'une seule fois. Ainsi, si vous essayez une autre boucle `for`, vous n'obtenez rien :

```python
>>> for n in squares:
...     print(n)
...
>>>
```
