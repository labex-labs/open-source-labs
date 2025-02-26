# Chargement de module et chemin du système

Essayez d'importer le module que vous venez de créer :

```python
>>> import simplemod
Chargé simplemod
>>> simplemod.foo()
x est 42
>>>
```

Si cela a échoué avec une `ImportError`, votre paramètre de chemin est instable. Regardez la valeur de `sys.path` et corrigez-la.

```python
>>> import sys
>>> sys.path
... regardez le résultat...
>>>
```
