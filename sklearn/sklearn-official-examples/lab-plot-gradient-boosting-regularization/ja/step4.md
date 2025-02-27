# 正則化戦略の実装

ここでは、さまざまな正則化戦略を実装し、それらの性能を比較します。

#### シュリンクレッジなし

まずはシュリンクレッジを行わず、学習率を 1 に設定します。

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 学習率 = 0.2

次に、学習率を 0.2 に設定し、サブサンプリングを 1 に設定します。

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### サブサンプリング = 0.5

ここで、サブサンプリングを 0.5 に設定し、学習率を 1 に設定します。

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 学習率 = 0.2 かつ サブサンプリング = 0.5

次に、学習率を 0.2 に設定し、サブサンプリングを 0.5 に設定します。

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 学習率 = 0.2 かつ 最大特徴数 = 2

最後に、学習率を 0.2 に設定し、各木に対して 2 つの特徴のみを使用します。

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```
