# Filtering Specific Rows

To select rows based on a conditional expression, use the condition inside the selection brackets `[]`.

```python
# Filter rows where 'Age' is greater than 35
above_35 = titanic[titanic["Age"] > 35]

# Display the first 5 rows
above_35.head()
```
