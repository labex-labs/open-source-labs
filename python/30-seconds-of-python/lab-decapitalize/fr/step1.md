# Décapitaliser une chaîne de caractères

Écrivez une fonction `decapitalize(s, upper_rest = False)` qui prend une chaîne de caractères `s` et renvoie une nouvelle chaîne de caractères avec la première lettre en minuscules. La fonction devrait également avoir un paramètre optionnel `upper_rest` qui, lorsqu'il est défini sur `True`, convertit le reste de la chaîne en majuscules.

```python
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
