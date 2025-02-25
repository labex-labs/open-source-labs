# Défi de la distance de Hamming

## Problème

Écrire une fonction `hamming_distance(a, b)` qui prend deux entiers en arguments et renvoie la distance de Hamming entre eux. La fonction doit effectuer les étapes suivantes :

1. Utiliser l'opérateur XOR (`^`) pour trouver la différence binaire entre les deux nombres.
2. Utiliser `bin()` pour convertir le résultat en une chaîne binaire.
3. Convertir la chaîne en une liste et utiliser `count()` de la classe `str` pour compter et renvoyer le nombre de `1` dans celle-ci.

## Exemple

```python
hamming_distance(2, 3) # 1
hamming_distance(10, 4) # 2
hamming_distance(0, 255) # 8
```
