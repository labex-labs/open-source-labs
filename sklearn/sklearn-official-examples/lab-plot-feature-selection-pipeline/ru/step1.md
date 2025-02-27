# Создание и разделение набора данных

Начнем с создания бинарного датасета классификации с использованием функции `make_classification` из Scikit-learn. Также разделим датасет на тренировочную и тестовую подмножества с использованием функции `train_test_split` из Scikit-learn.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(
    n_features=20,
    n_informative=3,
    n_redundant=0,
    n_classes=2,
    n_clusters_per_class=2,
    random_state=42,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
```
