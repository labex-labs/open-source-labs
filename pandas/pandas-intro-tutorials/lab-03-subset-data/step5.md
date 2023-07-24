# Selecting Specific Rows and Columns

To select both rows and columns in one go, we use the `loc` or `iloc` operators.

```python
# Select 'Name' of passengers older than 35
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Display the first 5 rows
adult_names.head()
```
