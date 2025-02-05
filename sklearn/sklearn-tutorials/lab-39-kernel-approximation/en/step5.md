# Polynomial Kernel Approximation via Tensor Sketch

The Polynomial kernel is a popular kernel function that models interactions between features. The PolynomialCountSketch class provides a scalable method for approximating this kernel using the TensorSketch approach.

To use PolynomialCountSketch for kernel approximation, follow these steps:

1. Initialize the PolynomialCountSketch object with the desired degree (d) and the number of components.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

degree = 3
n_components = 100
polynomial_count_sketch = PolynomialCountSketch(degree=degree, n_components=n_components)
```

2. Fit the PolynomialCountSketch object to your training data.

```python
polynomial_count_sketch.fit(X_train)
```

3. Transform your training and test data using the PolynomialCountSketch object.

```python
X_train_transformed = polynomial_count_sketch.transform(X_train)
X_test_transformed = polynomial_count_sketch.transform(X_test)
```
