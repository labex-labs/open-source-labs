# Cálculo del vector singular principal utilizando SVD aleatorizado

Calcularemos los vectores singulares principales utilizando el método randomized_svd implementado en scikit-learn.

```python
from sklearn.decomposition import randomized_svd

print("Calculando los vectores singulares principales utilizando randomized_svd")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
