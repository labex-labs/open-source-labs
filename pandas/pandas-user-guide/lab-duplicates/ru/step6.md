# Проверка и установка флага о дублирующихся метках

Наконец, мы можем проверить и установить флаг `allows_duplicate_labels` для DataFrame.

```python
# Creating a DataFrame and setting allows_duplicate_labels to False
df = pd.DataFrame({"A": [0, 1, 2, 3]}, index=["x", "y", "X", "Y"]).set_flags(allows_duplicate_labels=False)

# Checking the allows_duplicate_labels flag
print(df.flags.allows_duplicate_labels)

# Setting allows_duplicate_labels to True
df2 = df.set_flags(allows_duplicate_labels=True)
print(df2.flags.allows_duplicate_labels)
```
