# Palindrome

Écrivez une fonction `palindrome(s)` qui prend une chaîne de caractères `s` comme seul paramètre et renvoie `True` si `s` est un palindrome et `False` sinon. Votre fonction devrait ignorer la casse et les caractères non alphanumériques lors de la vérification des palindromes.

Pour résoudre ce problème, vous pouvez suivre les étapes suivantes :

1. Utilisez `str.lower()` pour convertir la chaîne en minuscules.
2. Utilisez `re.sub()` pour supprimer tous les caractères non alphanumériques de la chaîne.
3. Comparez la chaîne résultante avec sa version inversée en utilisant la notation de tranches.

```python
from re import sub

def palindrome(s):
  s = sub('[\W_]', '', s.lower())
  return s == s[::-1]
```

```python
palindrome('taco cat') # True
```
