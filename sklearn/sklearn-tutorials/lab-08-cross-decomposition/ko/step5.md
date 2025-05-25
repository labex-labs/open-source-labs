# CCA

#### CCA 모델 적합

`CCA` 알고리즘은 PLS 의 특수한 경우로, 표준 상관 분석 (Canonical Correlation Analysis) 을 의미합니다. 두 변수 집합 간의 상관관계를 찾습니다.

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### 데이터 변환

적합된 모델을 사용하여 원본 데이터를 변환할 수 있습니다. 변환된 데이터는 차원이 감소됩니다.

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```
