# NumPy 와의 차이점 이해

Pandas 와 NumPy 는 분산을 계산하는 방식에 약간의 차이가 있습니다. 두 라이브러리 간에 전환할 때 이를 고려하는 것이 중요합니다.

```python
# pandas 에서의 분산
var_pandas = df.var()

# NumPy 에서의 분산
var_numpy = np.var(df.values)
```
