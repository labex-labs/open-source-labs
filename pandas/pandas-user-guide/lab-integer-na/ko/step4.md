# pandas.NA 로 결측값 처리하기

`IntegerArray` 클래스는 스칼라 결측값으로 `pandas.NA`를 사용합니다. 결측된 단일 요소를 슬라이싱하면 `pandas.NA`를 반환합니다.

```python
# Create an IntegerArray with a missing value
a = pd.array([1, None], dtype="Int64")

# Slice the second element which is a missing value
missing_value = a[1]
# Output: <NA>
```
