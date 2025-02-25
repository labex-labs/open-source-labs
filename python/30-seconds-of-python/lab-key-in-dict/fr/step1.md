# Vérifier si une clé existe dans un dictionnaire

Écrivez une fonction `key_in_dict(d, key)` qui prend un dictionnaire `d` et une clé `key` en arguments et renvoie `True` si la clé existe dans le dictionnaire, `False` sinon.

```python
def key_in_dict(d, key):
  return (key in d)
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
```
