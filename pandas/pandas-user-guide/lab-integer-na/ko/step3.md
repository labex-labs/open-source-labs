# Nullable 정수 배열로 연산 수행하기

산술 연산, 비교 및 슬라이싱과 같은 다양한 연산을 nullable 정수 배열로 수행할 수 있습니다.

```python
# Create a Series with nullable integer type
s = pd.Series([1, 2, None], dtype="Int64")

# Perform arithmetic operation
s_plus_one = s + 1 # adds 1 to each element in the series

# Perform comparison
comparison = s == 1 # checks if each element in the series is equal to 1

# Perform slicing operation
sliced = s.iloc[1:3] # selects the second and third elements in the series
```
