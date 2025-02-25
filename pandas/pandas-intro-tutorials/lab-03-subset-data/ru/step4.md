# Фильтрация определенных строк

Для выбора строк на основе условного выражения используйте условие внутри квадратных скобок `[]`.

```python
# Filter rows where 'Age' is greater than 35
above_35 = titanic[titanic["Age"] > 35]

# Display the first 5 rows
above_35.head()
```
