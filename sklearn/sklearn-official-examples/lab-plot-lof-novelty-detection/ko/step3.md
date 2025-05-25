# 모델 학습

이제 훈련 데이터를 사용하여 LOF 모델을 학습시키겠습니다. 이웃 수를 20 으로 설정하고, novelty 를 True 로, contamination 을 0.1 로 설정합니다.

```python
clf = LocalOutlierFactor(n_neighbors=20, novelty=True, contamination=0.1)
clf.fit(X_train)
```
