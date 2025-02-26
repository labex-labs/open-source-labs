# Préparation

Nous allons recréer la classe `Stock` entièrement à partir de zéro en utilisant quelques nouvelles techniques. Assurez-vous d'avoir vos tests unitaires de l'exercice 5.4 prêts à portée de main. Vous en aurez besoin.

Si vous définissez une fonction, vous savez probablement déjà qu'elle peut être appelée en utilisant une combinaison d'arguments positionnels ou nommés. Par exemple :

```python
>>> def foo(x, y, z):
        return x + y + z

>>> foo(1, 2, 3)
6
>>> foo(1, z=3, y=2)
6
>>>
```

Vous savez peut-être également que vous pouvez passer des séquences et des dictionnaires en tant qu'arguments de fonction en utilisant la syntaxe `*` et `**`. Par exemple :

```python
>>> args = (1, 2, 3)
>>> foo(*args)
6
>>> kwargs = {'y':2, 'z':3 }
>>> foo(1,**kwargs)
6
>>>
```

En outre, vous pouvez écrire des fonctions qui acceptent un nombre quelconque d'arguments positionnels ou nommés en utilisant la syntaxe `*` et `**`. Par exemple :

```python
>>> def foo(*args):
        print(args)

>>> foo(1,2)
(1, 2)
>>> foo(1,2,3,4,5)
(1, 2, 3, 4, 5)
>>> foo()
()
>>>
>>> def bar(**kwargs):
        print(kwargs)

>>> bar(x=1,y=2)
{'y': 2, 'x': 1}
>>> bar(x=1,y=2,z=3)
{'y': 2, 'x': 1, 'z': 3}
>>> bar()
{}
>>>
```

Les fonctions à arguments variables sont parfois utiles comme une technique pour réduire ou simplifier la quantité de code que vous devez taper. Dans cet exercice, nous allons explorer cette idée pour des structures de données simples.
