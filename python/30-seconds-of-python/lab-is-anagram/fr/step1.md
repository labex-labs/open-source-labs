# Anagramme de chaîne de caractères

Écrivez une fonction `is_anagram(s1, s2)` qui prend deux chaînes de caractères en arguments et renvoie `True` si elles sont des anagrammes l'une de l'autre, et `False` sinon. La fonction doit être insensible à la casse, ignorer les espaces, la ponctuation et les caractères spéciaux.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez `str.isalnum()` pour filtrer les caractères non alphanumériques et `str.lower()` pour transformer chaque caractère en minuscules.
2. Utilisez `collections.Counter` pour compter les caractères résultants pour chaque chaîne et comparer les résultats.

```python
from collections import Counter

def is_anagram(s1, s2):
  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )
```

```python
is_anagram('#anagram', 'Nag a ram!')  # True
```
