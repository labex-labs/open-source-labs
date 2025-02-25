# Création d'une matrice aléatoire

Ensuite, nous allons créer une matrice aléatoire à l'aide de numpy. Nous utiliserons la méthode `rand` pour créer une matrice 5x3 avec des valeurs aléatoires comprises entre 0 et 1. Nous définirons également une graine aléatoire pour garantir la reproductibilité des résultats.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```
