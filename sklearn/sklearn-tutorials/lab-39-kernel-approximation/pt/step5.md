# Aproximação de Kernel Polinomial via Tensor Sketch

O kernel polinomial é uma função kernel popular que modela interações entre recursos. A classe PolynomialCountSketch fornece um método escalável para aproximar este kernel usando a abordagem TensorSketch.

Para usar PolynomialCountSketch para aproximação de kernel, siga estas etapas:

1. Inicialize o objeto PolynomialCountSketch com o grau desejado (d) e o número de componentes.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

degree = 3
n_components = 100
polynomial_count_sketch = PolynomialCountSketch(degree=degree, n_components=n_components)
```

2. Ajuste o objeto PolynomialCountSketch aos seus dados de treinamento.

```python
polynomial_count_sketch.fit(X_train)
```

3. Transforme seus dados de treinamento e teste usando o objeto PolynomialCountSketch.

```python
X_train_transformed = polynomial_count_sketch.transform(X_train)
X_test_transformed = polynomial_count_sketch.transform(X_test)
```
