# Pad String

Écrivez une fonction `pad(s: str, length: int, char: str = ' ') -> str` qui ajoute des caractères spécifiés des deux côtés d'une chaîne, si elle est plus courte que la longueur spécifiée. La fonction doit prendre trois paramètres :

- `s` : une chaîne qui doit être ajoutée
- `length` : un entier qui spécifie la longueur totale de la chaîne ajoutée
- `char` : un caractère utilisé pour ajouter des caractères à la chaîne. La valeur par défaut est un caractère d'espace.

La fonction doit renvoyer la chaîne ajoutée.

```python
from math import floor

def pad(s, length, char = ' '):
  return s.rjust(floor((len(s) + length)/2), char).ljust(length, char)
```

```python
pad('cat', 8) # '  cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```
