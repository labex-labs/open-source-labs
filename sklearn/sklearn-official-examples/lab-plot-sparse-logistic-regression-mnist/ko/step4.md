# 모델 학습

L1 페널티와 SAGA 알고리즘을 사용하여 로지스틱 회귀 모델을 학습합니다. `C` 값은 학습 샘플 수로 50.0 을 나눈 값으로 설정합니다.

```python
# 더 빠른 수렴을 위해 허용 오차를 높임
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
