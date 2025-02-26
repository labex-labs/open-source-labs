# Le chemin de recherche de modules

`sys.path` est un répertoire qui contient la liste de tous les répertoires vérifiés par l'instruction `import`. Voici ce que ça donne :

```python
>>> import sys
>>> sys.path
... regardez le résultat...
>>>
```

Si vous importez quelque chose et qu'il n'est pas situé dans l'un de ces répertoires, vous obtiendrez une exception `ImportError`.
