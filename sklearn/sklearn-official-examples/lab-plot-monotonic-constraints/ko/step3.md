# 제약 없이 모델 학습

생성된 데이터에 제약 없이 모델을 학습하여 제약 없이 모델이 어떻게 수행되는지 확인합니다.

```python
gbdt_no_cst = HistGradientBoostingRegressor()
gbdt_no_cst.fit(X, y)
```
