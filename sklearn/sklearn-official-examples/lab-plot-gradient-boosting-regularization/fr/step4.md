# Implémenter les stratégies de régularisation

Nous allons maintenant implémenter différentes stratégies de régularisation et comparer leurs performances.

#### Sans réduction

Nous commencerons sans réduction, ce qui signifie que le taux d'apprentissage sera fixé à 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Taux d'apprentissage = 0,2

Ensuite, nous fixerons le taux d'apprentissage à 0,2 et le sous-échantillonnage à 1.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Sous-échantillonnage = 0,5

Nous allons maintenant fixer le sous-échantillonnage à 0,5 et le taux d'apprentissage à 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Taux d'apprentissage = 0,2 et sous-échantillonnage = 0,5

Ensuite, nous fixerons le taux d'apprentissage à 0,2 et le sous-échantillonnage à 0,5.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Taux d'apprentissage = 0,2 et nombre maximum de caractéristiques = 2

Enfin, nous fixerons le taux d'apprentissage à 0,2 et utiliserons seulement 2 caractéristiques pour chaque arbre.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```
