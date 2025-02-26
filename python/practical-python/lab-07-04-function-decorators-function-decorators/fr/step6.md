# Exercice 7.10 : Un décorateur pour le chronométrage

Si vous définissez une fonction, son nom et son module sont stockés dans les attributs `__name__` et `__module__`. Par exemple :

```python
>>> def add(x,y):
        return x+y

>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>>
```

Dans un fichier `timethis.py`, écrivez une fonction décoratrice `timethis(func)` qui entoure une fonction d'une couche supplémentaire de logique qui imprime le temps qu'il prend pour une fonction s'exécuter. Pour ce faire, vous entourerez la fonction d'appels de chronométrage comme ceci :

```python
start = time.time()
r = func(*args,**kwargs)
end = time.time()
print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
```

Voici un exemple de fonctionnement de votre décorateur :

```python
>>> from timethis import timethis
>>> @timethis
def countdown(n):
    while n > 0:
        n -= 1

>>> countdown(10000000)
__main__.countdown : 0.076562
>>>
```

Discussion : Ce décorateur `@timethis` peut être placé devant n'importe quelle définition de fonction. Ainsi, vous pouvez l'utiliser comme outil de diagnostic pour l'optimisation des performances.
