# 특정 행 필터링

조건식에 따라 행을 선택하려면 선택 대괄호 `[]` 안에 조건을 사용합니다.

```python
# Filter rows where 'Age' is greater than 35
above_35 = titanic[titanic["Age"] > 35]

# Display the first 5 rows
above_35.head()
```
