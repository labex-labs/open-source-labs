# Understanding the Consequences of Duplicate Labels

Duplicate labels can change the behavior of certain operations in pandas. For instance, some methods do not work when duplicates are present.

```python
# Creating a pandas Series with duplicate labels
s1 = pd.Series([0, 1, 2], index=["a", "b", "b"])

# Attempting to reindex the Series
try:
    s1.reindex(["a", "b", "c"])
except Exception as e:
    print(e)
```
