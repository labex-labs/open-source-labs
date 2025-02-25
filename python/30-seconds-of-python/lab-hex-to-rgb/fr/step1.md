# Conversion hexadécimal en RGB

Écrivez une fonction `hex_to_rgb(hex_code)` qui prend un code de couleur hexadécimal sous forme de chaîne de caractères et renvoie un tuple d'entiers correspondant à ses composantes RGB. La fonction doit effectuer les étapes suivantes :

1. Utilisez une compréhension de liste en combinaison avec `int()` et la notation de tranches de liste pour obtenir les composantes RGB à partir de la chaîne hexadécimale.
2. Utilisez `tuple()` pour convertir la liste résultante en un tuple.

```python
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
```

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
