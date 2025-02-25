# Nombre en binaire

Écrivez une fonction `to_binary(n)` qui prend un nombre décimal en entrée et renvoie sa représentation binaire sous forme de chaîne de caractères. Votre fonction devrait effectuer les étapes suivantes :

1. Utilisez `bin()` pour convertir le nombre décimal en son équivalent binaire.
2. Retournez la représentation binaire sous forme de chaîne de caractères.

```python
def to_binary(n):
  return bin(n)
```

```python
to_binary(100) # 0b1100100
```
