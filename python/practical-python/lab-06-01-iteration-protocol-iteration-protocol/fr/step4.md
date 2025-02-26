# Exercice 6.1 : Illustration de l'itération

Créez la liste suivante :

```python
a = [1,9,4,25,16]
```

Itérez manuellement sur cette liste. Appelez `__iter__()` pour obtenir un itérateur et appelez la méthode `__next__()` pour obtenir les éléments successifs.

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

La fonction intégrée `next()` est un raccourci pour appeler la méthode `__next__()` d'un itérateur. Essayez de l'utiliser sur un fichier :

```python
>>> f = open('portfolio.csv')
>>> f.__iter__()    # Note : Cela renvoie le fichier lui-même
<_io.TextIOWrapper name='portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

Appelez `next(f)` jusqu'à la fin du fichier. Regardez ce qui se passe.
