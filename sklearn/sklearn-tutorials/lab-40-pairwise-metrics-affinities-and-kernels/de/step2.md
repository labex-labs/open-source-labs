# Kerne

Kerne sind Maße der Ähnlichkeit zwischen zwei Objekten. Sie können in verschiedenen Machine-Learning-Algorithmen verwendet werden, um nicht-lineare Beziehungen zwischen Merkmalen zu erfassen.

Scikit-learn bietet verschiedene Kernfunktionen an, wie die lineare Kernel, die polynomielle Kernel, die sigmoidale Kernel, die RBF-Kernel, die Laplace-Kernel und die chi-quadratische Kernel.

Lassen Sie uns die paarweisen Kerne zwischen zwei Mengen von Proben mit der Funktion `pairwise_kernels` berechnen:

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calculate pairwise kernels between X and Y using linear kernel
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

Ausgabe:

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```
