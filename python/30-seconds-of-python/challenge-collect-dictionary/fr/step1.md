# Inverser un dictionnaire

## Problème

Écrivez une fonction `invert_dictionary(obj)` qui prend un dictionnaire `obj` en entrée et renvoie un nouveau dictionnaire avec les clés et les valeurs inversées. Le dictionnaire d'entrée aura des valeurs hachables non uniques. Si deux ou plusieurs clés ont la même valeur, la fonction devrait ajouter les clés à une liste dans le dictionnaire de sortie.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Créez un `collections.defaultdict` avec `list` comme valeur par défaut pour chaque clé.
2. Utilisez `dictionary.items()` en combinaison avec une boucle pour mapper les valeurs du dictionnaire aux clés en utilisant `dict.append()`.
3. Utilisez `dict()` pour convertir le `collections.defaultdict` en un dictionnaire classique.

Signature de la fonction : `def invert_dictionary(obj: dict) -> dict:`

## Exemple

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
