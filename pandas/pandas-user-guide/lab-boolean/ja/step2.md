# NA 値を使ったインデックス付け

Pandas は、ブール配列で`NA`値を使ったインデックス付けを許可しており、これらは`False`として扱われます。

```python
# Creating a pandas Series
s = pd.Series([1, 2, 3])

# Creating a boolean array with NA values
mask = pd.array([True, False, pd.NA], dtype="boolean")

# Indexing the series with the boolean array
s[mask] # NA values are treated as False
```

`NA`値を維持したい場合は、`fillna(True)`で手動で埋めることができます。

```python
# Filling NA values with True and indexing the series
s[mask.fillna(True)]
```
