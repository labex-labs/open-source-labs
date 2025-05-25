# 조기 종료 없이 모델 구축 및 학습

이제 조기 종료 없이 경사 부스팅 모델을 구축하고 학습합니다.

```python
gb = ensemble.GradientBoostingClassifier(n_estimators=n_estimators, random_state=0)
start = time.time()
gb.fit(X_train, y_train)
time_gb.append(time.time() - start)
```
