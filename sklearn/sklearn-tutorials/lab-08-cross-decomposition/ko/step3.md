# PLSRegression

#### PLSRegression 모델 적합

정규화된 선형 회귀의 한 형태인 `PLSRegression` 알고리즘으로 시작합니다. 모델을 데이터에 적합시킵니다.

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### 데이터 변환

적합된 모델을 사용하여 원본 데이터를 변환할 수 있습니다. 변환된 데이터는 차원이 감소됩니다.

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```
