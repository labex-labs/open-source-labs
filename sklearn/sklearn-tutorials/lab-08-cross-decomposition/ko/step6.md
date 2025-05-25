# PLSSVD

#### PLSSVD 모델 적합

`PLSSVD` 알고리즘은 `PLSCanonical`의 간소화된 버전으로, 교차 공분산 행렬의 특이값 분해 (Singular Value Decomposition, SVD) 를 단 한 번만 계산합니다. 이 알고리즘은 주성분의 수가 하나로 제한될 때 유용합니다.

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### 데이터 변환

적합된 모델을 사용하여 원본 데이터를 변환할 수 있습니다. 변환된 데이터는 차원이 감소됩니다.

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```
