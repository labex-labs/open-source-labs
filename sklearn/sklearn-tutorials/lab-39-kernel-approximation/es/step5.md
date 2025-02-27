# Aproximación del Kernel Polinomial a través del Bosquejo de Tensor

El kernel polinomial es una función de kernel popular que modela las interacciones entre las características. La clase PolynomialCountSketch proporciona un método escalable para aproximar este kernel utilizando el enfoque de Bosquejo de Tensor.

Para utilizar PolynomialCountSketch para la aproximación de kernel, siga estos pasos:

1. Inicialice el objeto PolynomialCountSketch con el grado deseado (d) y el número de componentes.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

degree = 3
n_components = 100
polynomial_count_sketch = PolynomialCountSketch(degree=degree, n_components=n_components)
```

2. Ajuste el objeto PolynomialCountSketch a sus datos de entrenamiento.

```python
polynomial_count_sketch.fit(X_train)
```

3. Transforme sus datos de entrenamiento y prueba utilizando el objeto PolynomialCountSketch.

```python
X_train_transformed = polynomial_count_sketch.transform(X_train)
X_test_transformed = polynomial_count_sketch.transform(X_test)
```
