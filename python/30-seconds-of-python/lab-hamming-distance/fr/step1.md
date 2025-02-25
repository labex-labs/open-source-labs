# Distance de Hamming

Écrivez une fonction `hamming_distance(a, b)` qui prend deux entiers en arguments et renvoie la distance de Hamming entre eux. La fonction doit effectuer les étapes suivantes :

1. Utilisez l'opérateur XOR (`^`) pour trouver la différence binaire entre les deux nombres.
2. Utilisez `bin()` pour convertir le résultat en une chaîne binaire.
3. Convertissez la chaîne en une liste et utilisez `count()` de la classe `str` pour compter et renvoyer le nombre de `1` dans celle-ci.

```python
def hamming_distance(a, b):
  return bin(a ^ b).count('1')
```

```python
hamming_distance(2, 3) # 1
```
