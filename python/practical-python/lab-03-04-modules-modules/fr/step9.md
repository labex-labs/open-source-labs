# Chargement des modules

Chaque module ne se charge et n'est exécuté qu'_une seule fois_. _Remarque : Les importations répétées ne renvoient simplement qu'une référence au module chargé précédemment._

`sys.modules` est un dictionnaire de tous les modules chargés.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__','site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath',...]
>>>
```

**Attention** : Une erreur fréquente se produit si vous répétez une instruction `import` après avoir modifié le code source d'un module. En raison du cache des modules `sys.modules`, les importations répétées renvoient toujours le module chargé précédemment - même si un changement a été effectué. Le moyen le plus sûr de charger le code modifié dans Python est d'arrêter et de redémarrer l'interpréteur.
