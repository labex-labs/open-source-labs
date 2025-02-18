# Generar datos sintéticos

A continuación, generaremos datos sintéticos para demostrar la diferencia entre LDA y QDA. Utilizaremos la función `make_classification` de scikit-learn para crear dos clases con patrones distintos.

```python
from sklearn.datasets import make_classification

# Generate synthetic data
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, random_state=1)
```
