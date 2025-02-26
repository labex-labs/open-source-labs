# Chargement répété de module

Assurez-vous de comprendre que les modules ne sont chargés qu'une seule fois. Essayez une importation répétée et remarquez comment vous ne voyez pas la sortie de la fonction `print` :

```python
>>> import simplemod
>>>
```

Essayez de modifier la valeur de `x` et constatez qu'une importation répétée n'a aucun effet.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> import simplemod
>>> simplemod.x
13
>>>
```

Utilisez `importlib.reload()` si vous voulez forcer le rechargement d'un module.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Chargé simplemod
<module'simplemod' from'simplemod.py'>
>>> simplemod.x
42
>>>
```

`sys.modules` est un dictionnaire de tous les modules chargés. Jetez un œil dessus, supprimez votre module et essayez une importation répétée.

```python
>>> sys.modules
... regardez la sortie...
>>> sys.modules['simplemod']
<module'simplemod' from'simplemod.py'>
>>> del sys.modules['simplemod']
>>> import simplemod
Chargé simplemod
>>>
```
