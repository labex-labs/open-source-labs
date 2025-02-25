# Conversion hexadécimal en RGB

## Problème

Écrivez une fonction `hex_to_rgb(hex_code)` qui prend un code de couleur hexadécimal sous forme de chaîne de caractères et renvoie un tuple d'entiers correspondant à ses composantes RGB. La fonction doit effectuer les étapes suivantes :

1. Utilisez une compréhension de liste en combinaison avec `int()` et la notation de tranche de liste pour obtenir les composantes RGB à partir de la chaîne hexadécimale.
2. Utilisez `tuple()` pour convertir la liste résultante en un tuple.

## Exemple

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
