# Implement Regularization Strategies

We will now implement different regularization strategies and compare their performance.

#### No Shrinkage

We will start with no shrinkage, which means the learning rate will be set to 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Learning Rate = 0.2

Next, we will set the learning rate to 0.2 and subsample to 1.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Subsample = 0.5

We will now set the subsample to 0.5 and the learning rate to 1.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Learning Rate = 0.2 and Subsample = 0.5

Next, we will set the learning rate to 0.2 and subsample to 0.5.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### Learning Rate = 0.2 and Max Features = 2

Finally, we will set the learning rate to 0.2 and use only 2 features for each tree.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```


