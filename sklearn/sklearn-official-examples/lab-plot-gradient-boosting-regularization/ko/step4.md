# 정규화 전략 구현

이제 다양한 정규화 전략을 구현하고 성능을 비교합니다.

#### 축소 없음

먼저 축소를 적용하지 않고 학습률을 1 로 설정합니다.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 학습률 = 0.2

다음으로 학습률을 0.2 로, 샘플링 비율 (subsample) 을 1 로 설정합니다.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 1.0})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 샘플링 비율 = 0.5

이제 샘플링 비율 (subsample) 을 0.5 로, 학습률을 1 로 설정합니다.

```python
params = dict(original_params)
params.update({"learning_rate": 1.0, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 학습률 = 0.2 및 샘플링 비율 = 0.5

다음으로 학습률을 0.2 로, 샘플링 비율 (subsample) 을 0.5 로 설정합니다.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "subsample": 0.5})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```

#### 학습률 = 0.2 및 최대 특징 = 2

마지막으로 학습률을 0.2 로 설정하고 각 트리에 2 개의 특징만 사용합니다.

```python
params = dict(original_params)
params.update({"learning_rate": 0.2, "max_features": 2})

clf = ensemble.GradientBoostingClassifier(**params)
clf.fit(X_train, y_train)
```
