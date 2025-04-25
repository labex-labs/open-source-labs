# 实施正则化策略

我们现在将实施不同的正则化策略并比较它们的性能。

#### 无收缩

我们将从无收缩开始，这意味着学习率将设置为 1。

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 学习率 = 0.2

接下来，我们将学习率设置为 0.2，子采样设置为 1。

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 子采样 = 0.5

我们现在将子采样设置为 0.5，学习率设置为 1。

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 学习率 = 0.2 且 子采样 = 0.5

接下来，我们将学习率设置为 0.2，子采样设置为 0.5。

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 学习率 = 0.2 且 最大特征数 = 2

最后，我们将学习率设置为 0.2，并且每棵树仅使用 2 个特征。

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```
