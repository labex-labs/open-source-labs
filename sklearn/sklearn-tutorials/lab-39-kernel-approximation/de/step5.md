# Polynomkernel-Approximation über Tensor Sketch

Der Polynomkernel ist eine beliebte Kernel-Funktion, die Interaktionen zwischen Merkmalen modelliert. Die PolynomialCountSketch-Klasse bietet eine skalierbare Methode zur Approximation dieses Kerns unter Verwendung des TensorSketch-Ansatzes.

Um PolynomialCountSketch zur Kernel-Approximation zu verwenden, führen Sie die folgenden Schritte aus:

1. Initialisieren Sie das PolynomialCountSketch-Objekt mit dem gewünschten Grad (d) und der Anzahl der Komponenten.

```python
from sklearn.kernel_approximation import PolynomialCountSketch

degree = 3
n_components = 100
polynomial_count_sketch = PolynomialCountSketch(degree=degree, n_components=n_components)
```

2. Passen Sie das PolynomialCountSketch-Objekt an Ihre Trainingsdaten an.

```python
polynomial_count_sketch.fit(X_train)
```

3. Transformieren Sie Ihre Trainings- und Testdaten mit dem PolynomialCountSketch-Objekt.

```python
X_train_transformed = polynomial_count_sketch.transform(X_train)
X_test_transformed = polynomial_count_sketch.transform(X_test)
```
