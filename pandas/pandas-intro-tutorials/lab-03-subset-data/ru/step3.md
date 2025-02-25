# Выбор нескольких столбцов

Для выбора нескольких столбцов используйте список имен столбцов внутри квадратных скобок `[]`.

```python
# Select the 'Age' and 'Sex' columns
age_sex = titanic[["Age", "Sex"]]

# Display the first 5 rows
age_sex.head()
```
