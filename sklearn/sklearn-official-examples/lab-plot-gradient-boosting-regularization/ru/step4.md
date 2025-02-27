# Реализуем стратегии регуляризации

Теперь мы реализуем различные стратегии регуляризации и сравним их производительность.

#### Без уменьшения (shrinkage)

Начнем с отсутствия уменьшения, что означает, что коэффициент обучения будет установлен равным 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Коэффициент обучения = 0.2

Далее установим коэффициент обучения равным 0.2 и долю выборки равной 1.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Доля выборки = 0.5

Теперь установим долю выборки равной 0.5 и коэффициент обучения равным 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Коэффициент обучения = 0.2 и доля выборки = 0.5

Далее установим коэффициент обучения равным 0.2 и долю выборки равной 0.5.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Коэффициент обучения = 0.2 и максимальное количество признаков = 2

Наконец, установим коэффициент обучения равным 0.2 и для каждого дерева будем использовать только 2 признака.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```
