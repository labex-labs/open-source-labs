# Revoir la mémoire

Dans les données du bus CTA, nous avons déterminé qu'il y avait 181 itinéraires de bus uniques.

```python
>>> routes = { row['route'] for row in rows }
>>> len(routes)
181
>>>
```

Question : Combien d'objets de chaîne d'itinéraire uniques sont contenus dans les données de trajet? Au lieu de construire un ensemble d'itinéraires, construisons un ensemble d'identifiants d'objets :

```python
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
542305
>>>
```

Pensez-y un moment - il n'y a que 181 noms d'itinéraire distincts, mais la liste de dictionnaires résultante contient 542305 chaînes d'itinéraire différentes. Peut-être que cela pourrait être corrigé avec un peu de mise en cache ou de réutilisation d'objets. Il s'avère que Python a une fonction qui peut être utilisée pour mettre en cache les chaînes, `sys.intern()`. Par exemple :

```python
>>> a = 'hello world'
>>> b = 'hello world'
>>> a is b
False
>>> import sys
>>> a = sys.intern(a)
>>> b = sys.intern(b)
>>> a is b
True
>>>
```

Redémarrez Python et essayez cela :

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, str, str, int])
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
181
>>>
````

Regardez l'utilisation de la mémoire.

```python
>>> tracemalloc.get_traced_memory()
... regardez le résultat...
>>>
```

La mémoire devrait baisser considérablement. Observation : Il y a également beaucoup de répétition concernant les dates. Que se passe-t-il si vous mettez également en cache les chaînes de dates?

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, str, int])
>>> tracemalloc.get_traced_memory()
... regardez le résultat...
>>>
````
