# 데이터 정렬 및 산술 연산

데이터 정렬은 pandas 의 중요한 기능입니다. 두 객체에 대해 연산을 수행할 때, pandas 는 연관된 레이블을 기준으로 정렬합니다.

```python
# Create two DataFrames
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# Perform addition operation
result = df1 + df2
```
