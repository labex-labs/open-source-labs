# Trouver la clé d'une valeur dans un dictionnaire

## Problème

Écrivez une fonction `trouver_cle(dict, val)` qui trouve la première clé dans le dictionnaire fourni qui a la valeur donnée.

Votre fonction doit :

- Prendre un dictionnaire `dict` et une valeur `val` en entrée.
- Utiliser `dictionary.items()` et `next()` pour renvoyer la première clé qui a une valeur égale à `val`.
- Retourner la clé en tant que sortie.

## Exemple

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
trouver_cle(ages, 11) # 'Isabel'
```
