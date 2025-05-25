# Cálculo do Vetor Singular Principal usando SVD Aleatorizado

Calcularemos os vetores singulares principais usando o método `randomized_svd` implementado no scikit-learn.

```python
from sklearn.decomposition import randomized_svd

print("Calculando os vetores singulares principais usando randomized_svd")
U, s, V = randomized_svd(X, 5, n_iter=3)
```
