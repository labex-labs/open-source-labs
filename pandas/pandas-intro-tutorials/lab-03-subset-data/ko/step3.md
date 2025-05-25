# 여러 열 선택

여러 열을 선택하려면 선택 대괄호 `[]` 안에 열 이름 목록을 사용합니다.

```python
# Select the 'Age' and 'Sex' columns
age_sex = titanic[["Age", "Sex"]]

# Display the first 5 rows
age_sex.head()
```
