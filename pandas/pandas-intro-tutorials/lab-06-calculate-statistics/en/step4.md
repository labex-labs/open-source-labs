# Counting Number of Records by Category

Finally, we will count the number of records by category.

```python
# Counting the number of passengers in each of the cabin classes
passengers_per_class = titanic["Pclass"].value_counts()
# Printing the result
print(f"The number of passengers in each of the cabin classes is {passengers_per_class}")
```
