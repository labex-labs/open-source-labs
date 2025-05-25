# 특징 개수 유지

기본적으로 scikit-learn 임퓨터는 누락된 값만 포함하는 열을 삭제합니다. 하지만, 데이터의 형태를 유지하기 위해 빈 특징을 유지해야 하는 경우가 있습니다. 이를 위해 `keep_empty_features` 매개변수를 True 로 설정하면 됩니다.

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
