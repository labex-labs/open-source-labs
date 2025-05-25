# PLSCanonical

#### PLSCanonical 모델 적합

다음으로, 두 행렬 간의 표준 상관관계를 찾는 `PLSCanonical` 알고리즘을 사용합니다. 이 알고리즘은 특징들 간의 다중 공선성이 있을 때 유용합니다.

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### 데이터 변환

적합된 모델을 사용하여 원본 데이터를 변환할 수 있습니다. 변환된 데이터는 차원이 감소됩니다.

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```
