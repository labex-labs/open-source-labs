# Noyau polynomial

Le noyau polynomial calcule la similarité entre deux vecteurs en considérant les interactions entre leurs dimensions.

Scikit-learn fournit la fonction `polynomial_kernel` pour calculer le noyau polynomial entre des vecteurs.

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute polynomial kernel between X and Y
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

Sortie :

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```
