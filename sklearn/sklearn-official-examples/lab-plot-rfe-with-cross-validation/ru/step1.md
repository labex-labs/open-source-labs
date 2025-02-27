# Генерация данных

Мы сгенерируем задачу классификации с использованием функции `make_classification` из scikit-learn. Мы сгенерируем 500 выборок с 15 признаками, из которых 3 информативных, 2 избыточных и 10 неинформативных.

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
