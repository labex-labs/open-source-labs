# Загрузка и подготовка данных

Далее мы загрузим и подготовим данные. Мы загрузим датасет Iris с использованием scikit-learn и выберем только два признака. Затем мы разделим данные на обучающий и тестовый наборы.

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# we only take two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.7, random_state=42
)
```
