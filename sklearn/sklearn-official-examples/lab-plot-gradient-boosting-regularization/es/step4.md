# Implementar estrategias de regularización

Ahora implementaremos diferentes estrategias de regularización y compararemos su rendimiento.

#### Sin contracción

Comenzaremos sin contracción, lo que significa que la tasa de aprendizaje se establecerá en 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Tasa de aprendizaje = 0.2

A continuación, estableceremos la tasa de aprendizaje en 0.2 y el submuestreo en 1.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Submuestreo = 0.5

Ahora estableceremos el submuestreo en 0.5 y la tasa de aprendizaje en 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Tasa de aprendizaje = 0.2 y Submuestreo = 0.5

A continuación, estableceremos la tasa de aprendizaje en 0.2 y el submuestreo en 0.5.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Tasa de aprendizaje = 0.2 y Máximo de características = 2

Finalmente, estableceremos la tasa de aprendizaje en 0.2 y usaremos solo 2 características para cada árbol.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```
