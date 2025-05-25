# NA 값을 사용한 인덱싱

Pandas 는 부울 배열에서 `NA` 값을 사용한 인덱싱을 허용하며, 이는 `False`로 처리됩니다.

```python
# pandas Series 생성
s = pd.Series([1, 2, 3])

# NA 값을 가진 부울 배열 생성
mask = pd.array([True, False, pd.NA], dtype="boolean")

# 부울 배열로 시리즈 인덱싱
s[mask] # NA 값은 False 로 처리됨
```

`NA` 값을 유지하려면, `fillna(True)`를 사용하여 수동으로 채울 수 있습니다.

```python
# NA 값을 True 로 채우고 시리즈 인덱싱
s[mask.fillna(True)]
```
