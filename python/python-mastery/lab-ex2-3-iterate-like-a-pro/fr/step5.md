# Expressions génératrices

Une expression génératrice est presque exactement la même qu'une compréhension de liste, sauf qu'elle ne crée pas une liste. Au lieu de cela, elle crée un objet qui produit les résultats de manière incrémentielle - généralement pour être utilisé par itération. Essayez un exemple simple :

```python
>>> nums = [1,2,3,4,5]
>>> squares = (x*x for x in nums)
>>> squares
<generator object <genexpr> at 0x37caa8>
>>> for n in squares:
        print(n)

1
4
9
16
25
>>>
```

Vous remarquerez qu'une expression génératrice ne peut être utilisée qu'une seule fois. Regardez ce qui se passe si vous refaites la boucle `for` :

```python
>>> for n in squares:
         print(n)

>>>
```

Vous pouvez obtenir manuellement les résultats un par un si vous utilisez la fonction `next()`. Essayez ceci :

```python
>>> squares = (x*x for x in nums)
>>> next(squares)
1
>>> next(squares)
4
>>> next(squares)
9
>>>
```

Continuez à taper `next()` pour voir ce qui se passe lorsqu'il n'y a plus de données.

Si la tâche que vous effectuez est plus compliquée, vous pouvez toujours profiter des générateurs en écrivant une fonction génératrice et en utilisant l'instruction `yield` à la place. Par exemple :

```python
>>> def squares(nums):
        for x in nums:
            yield x*x

>>> for n in squares(nums):
        print(n)

1
4
9
16
25
>>>
```

Nous reviendrons sur les fonctions génératrices un peu plus tard dans le cours - pour l'instant, considérez simplement de telles fonctions comme ayant la propriété intéressante de fournir des valeurs à l'instruction `for`.
