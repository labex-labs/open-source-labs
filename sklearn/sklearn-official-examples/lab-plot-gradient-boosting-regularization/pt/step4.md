# Implementar Estratégias de Regularização

Agora, implementaremos diferentes estratégias de regularização e compararemos seu desempenho.

#### Sem Encolhimento

Começaremos sem encolhimento, o que significa que a taxa de aprendizado será definida como 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Taxa de Aprendizado = 0,2

Em seguida, definiremos a taxa de aprendizado como 0,2 e o subsample como 1.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Subsample = 0,5

Agora, definiremos o subsample como 0,5 e a taxa de aprendizado como 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Taxa de Aprendizado = 0,2 e Subsample = 0,5

Em seguida, definiremos a taxa de aprendizado como 0,2 e o subsample como 0,5.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Taxa de Aprendizado = 0,2 e Máximo de Características = 2

Finalmente, definiremos a taxa de aprendizado como 0,2 e usaremos apenas 2 características para cada árvore.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```
