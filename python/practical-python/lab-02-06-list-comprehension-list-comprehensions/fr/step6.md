# Exercice 2.19 : Compréhensions de liste

Essayez quelques compréhensions de liste simples pour vous familiariser avec la syntaxe.

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

Remarquez comment les compréhensions de liste créent une nouvelle liste avec les données convenablement transformées ou filtrées.
