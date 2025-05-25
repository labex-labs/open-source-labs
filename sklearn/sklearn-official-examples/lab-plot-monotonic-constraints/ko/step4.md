# 단조 제약 조건을 갖는 모델 학습

이제 동일한 데이터에 단조 제약 조건을 적용하여 다른 모델을 학습합니다. 첫 번째 특징에 단조 증가 제약 조건을, 두 번째 특징에 단조 감소 제약 조건을 적용합니다.

```python
gbdt_with_monotonic_cst = HistGradientBoostingRegressor(monotonic_cst=[1, -1])
gbdt_with_monotonic_cst.fit(X, y)
```
