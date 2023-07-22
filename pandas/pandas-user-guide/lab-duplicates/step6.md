# Checking and Setting the Duplicate Labels Flag

Finally, we can check and set the `allows_duplicate_labels` flag on a DataFrame.

```python
# Creating a DataFrame and setting allows_duplicate_labels to False
df = pd.DataFrame({"A": [0, 1, 2, 3]}, index=["x", "y", "X", "Y"]).set_flags(allows_duplicate_labels=False)

# Checking the allows_duplicate_labels flag
print(df.flags.allows_duplicate_labels)

# Setting allows_duplicate_labels to True
df2 = df.set_flags(allows_duplicate_labels=True)
print(df2.flags.allows_duplicate_labels)
```
