# Duplicates in Indexing

Next, we will look at how duplicates in indexing can lead to unexpected results.

```python
# Creating a DataFrame with duplicate column labels
df1 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "A", "B"])

# Indexing 'B' returns a Series
print(df1["B"])

# Indexing 'A' returns a DataFrame
print(df1["A"])
```
