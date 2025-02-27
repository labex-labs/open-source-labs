# Regularisierungstrategien implementieren

Wir werden nun verschiedene Regularisierungstrategien implementieren und deren Leistung vergleichen.

#### Keine Schrumpfung

Wir beginnen mit keiner Schrumpfung, was bedeutet, dass die Lernrate auf 1 gesetzt wird.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Lernrate = 0,2

Als nächstes setzen wir die Lernrate auf 0,2 und das Subsample auf 1.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Subsample = 0,5

Wir setzen nun das Subsample auf 0,5 und die Lernrate auf 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Lernrate = 0,2 und Subsample = 0,5

Als nächstes setzen wir die Lernrate auf 0,2 und das Subsample auf 0,5.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Lernrate = 0,2 und maximale Anzahl von Merkmalen = 2

Schließlich setzen wir die Lernrate auf 0,2 und verwenden nur 2 Merkmale für jeden Baum.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```
