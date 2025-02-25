# Commentaire

Au fur et à mesure que vous commencez à expérimenter avec l'interpréteur, vous voulez souvent en savoir plus sur les opérations prises en charge par différents objets. Par exemple, comment découvrir quelles opérations sont disponibles sur une chaîne de caractères?

Selon votre environnement Python, vous devriez peut-être être en mesure de voir une liste des méthodes disponibles via la complétion par tabulation. Par exemple, essayez d'entrer ceci :

```python
>>> s = 'hello world'
>>> s.<tabulation>
>>>
```

Si appuyer sur la touche Tab ne produit aucun effet, vous pouvez recourir à la fonction intégrée `dir()`. Par exemple :

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__',..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip','split','splitlines','startswith','strip','swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` produit une liste de toutes les opérations qui peuvent apparaître après le `(.)`. Utilisez la commande `help()` pour obtenir plus d'informations sur une opération spécifique :

```python
>>> help(s.upper)
Aide sur la fonction intégrée upper :

upper(...)
    S.upper() -> chaîne de caractères

    Retourne une copie de la chaîne de caractères S convertie en majuscules.
>>>
```
