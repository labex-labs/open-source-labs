# Nombre en hexadécimal

Écrivez une fonction `to_hex(dec)` qui prend un nombre décimal en argument et renvoie sa représentation hexadécimale. Votre fonction devrait effectuer les étapes suivantes :

1. Utilisez `hex()` pour convertir le nombre décimal en son équivalent hexadécimal.
2. Retournez la représentation hexadécimale.

```python
def to_hex(dec):
  return hex(dec)
```

```python
to_hex(41) # 0x29
to_hex(332) # 0x14c
```
