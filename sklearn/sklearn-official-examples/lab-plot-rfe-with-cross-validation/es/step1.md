# Generación de datos

Generaremos una tarea de clasificación utilizando la función `make_classification` de scikit-learn. Generaremos 500 muestras con 15 características, de las cuales 3 son informativas, 2 son redundantes y 10 son no informativas.

```python
from sklearn.datasets import make_classification

X, y = make_classification(
    n_samples=500,
    n_features=15,
    n_informative=3,
    n_redundant=2,
    n_repeated=0,
    n_classes=8,
    n_clusters_per_class=1,
    class_sep=0.8,
    random_state=0,
)
```
