# Création d'un tableau aléatoire

Ensuite, nous allons créer un tableau aléatoire de dimensions (20, 20) à l'aide de la fonction `numpy.random.randn`. Nous allons également définir quelques éléments sur zéro pour créer une matrice creuse.

```python
np.random.seed(19680801)
x = np.random.randn(20, 20)
x[5, :] = 0.
x[:, 12] = 0.
```
