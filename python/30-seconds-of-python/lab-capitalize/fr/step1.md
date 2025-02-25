# Capitalize String

Écrivez une fonction Python appelée `capitalize_string(s, lower_rest=False)` qui prend une chaîne de caractères en argument et renvoie une nouvelle chaîne de caractères avec la première lettre en majuscule. La fonction devrait avoir un paramètre optionnel `lower_rest` qui, s'il est défini sur `True`, convertit le reste de la chaîne en minuscules.

```python
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```python
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
