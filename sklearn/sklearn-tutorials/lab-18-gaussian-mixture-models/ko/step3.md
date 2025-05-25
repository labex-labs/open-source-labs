# 가우시안 혼합 모델 적합

이제 `sklearn.mixture` 모듈의 `GaussianMixture` 클래스를 사용하여 데이터에 가우시안 혼합 모델을 적합시킬 수 있습니다. 원하는 구성 요소 수와 사용할 다른 매개변수를 지정하십시오.

```python
# 가우시안 혼합 모델 적합
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
