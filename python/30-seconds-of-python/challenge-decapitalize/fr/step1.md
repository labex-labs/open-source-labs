# Décapitaliser une chaîne de caractères

## Problème

Écrivez une fonction `decapitalize(s, upper_rest = False)` qui prend une chaîne de caractères `s` et renvoie une nouvelle chaîne avec la première lettre en minuscules. La fonction devrait également avoir un paramètre optionnel `upper_rest` qui, lorsqu'il est défini sur `True`, convertit le reste de la chaîne en majuscules.

## Exemple

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
