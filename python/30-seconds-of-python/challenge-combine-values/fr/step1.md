# Combine Dictionary Values

## Problème

Écrivez une fonction `combine_values(*dicts)` qui prend deux ou plusieurs dictionnaires en arguments et renvoie un nouveau dictionnaire qui combine les valeurs des dictionnaires d'entrée. La fonction devrait effectuer les étapes suivantes :

1. Créez un nouveau `collections.defaultdict` avec `list` comme valeur par défaut pour chaque clé.
2. Parcourez les dictionnaires d'entrée et pour chaque dictionnaire :
   - Parcourez les clés du dictionnaire.
   - Ajoutez la valeur de la clé à la liste des valeurs pour cette clé dans le `defaultdict`.
3. Convertissez le `defaultdict` en un dictionnaire classique en utilisant la fonction `dict()`.
4. Retournez le dictionnaire résultant.

La fonction devrait avoir la signature suivante :

```python
def combine_values(*dicts):
    pass
```

## Exemple

```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```
