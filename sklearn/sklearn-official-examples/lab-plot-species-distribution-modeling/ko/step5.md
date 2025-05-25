# OneClassSVM 모델 학습

이 단계에서는 OneClassSVM 모델을 학습 데이터에 맞춥니다. 특징을 표준화하고 OneClassSVM 모델을 학습 데이터에 맞춥니다.

```python
# 특징 표준화
mean = BV_bunch.cov_train.mean(axis=0)
std = BV_bunch.cov_train.std(axis=0)
train_cover_std = (BV_bunch.cov_train - mean) / std

# OneClassSVM 모델 학습
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.5)
clf.fit(train_cover_std)
```
