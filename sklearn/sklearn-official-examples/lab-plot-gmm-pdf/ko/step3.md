# 가우시안 혼합 모델 적합

이제 scikit-learn 의 GaussianMixture 클래스를 사용하여 데이터셋에 GMM 을 적합시킵니다. 구성 요소 수를 2 개로, 공분산 유형을 "full"로 설정합니다.

```python
# 두 개의 구성 요소를 가진 가우시안 혼합 모델 적합
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```
