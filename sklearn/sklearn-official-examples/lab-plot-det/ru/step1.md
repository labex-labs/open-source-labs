# Генерация синтетических данных

Мы будем использовать функцию `make_classification` из scikit - learn для генерации синтетических данных. Эта функция генерирует случайную задачу классификации на n классов, с n_informative информативными признаками, n_redundant избыточными признаками и n_clusters_per_class кластерами для каждого класса. Мы сгенерируем 1000 образцов с 2 информативными признаками и случайным состоянием 1. Затем мы разделим данные на обучающую и тестовую выборки в соотношении 60/40.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1_000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1,
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
