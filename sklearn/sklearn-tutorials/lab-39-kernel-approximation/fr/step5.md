# Approximation du noyau polynomial via Tensor Sketch

Le noyau polynomial est une fonction noyau populaire qui modélise les interactions entre les caractéristiques. La classe PolynomialCountSketch fournit une méthode scalable pour approximer ce noyau en utilisant l'approche TensorSketch.

Pour utiliser PolynomialCountSketch pour l'approximation de noyau, suivez ces étapes :

1. Initialisez l'objet PolynomialCountSketch avec le degré souhaité (d) et le nombre de composants.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

degree = 3
n_components = 100
polynomial_count_sketch = PolynomialCountSketch(degree=degree, n_components=n_components)
```

2. Ajustez l'objet PolynomialCountSketch aux données d'entraînement.

```python
polynomial_count_sketch.fit(X_train)
```

3. Transformez vos données d'entraînement et de test à l'aide de l'objet PolynomialCountSketch.

```python
X_train_transformed = polynomial_count_sketch.transform(X_train)
X_test_transformed = polynomial_count_sketch.transform(X_test)
```
