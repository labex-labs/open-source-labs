# 인덱싱에서의 중복

다음으로, 인덱싱에서 중복이 예상치 못한 결과를 초래할 수 있는 방법을 살펴보겠습니다.

```python
# Creating a DataFrame with duplicate column labels
df1 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "A", "B"])

# Indexing 'B' returns a Series
print(df1["B"])

# Indexing 'A' returns a DataFrame
print(df1["A"])
```
