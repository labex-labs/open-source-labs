# 특정 행과 열 선택

한 번에 행과 열을 모두 선택하려면 `loc` 또는 `iloc` 연산자를 사용합니다.

```python
# Select 'Name' of passengers older than 35
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Display the first 5 rows
adult_names.head()
```
