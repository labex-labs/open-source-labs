# Загрузка набора данных

Функция `make_classification` из модуля `sklearn.datasets` используется для генерации набора данных для классификации. Набор данных содержит 400 образцов с 12 признаками. Код для загрузки набора данных выглядит следующим образом:

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```
