# Das Verbot von doppelten Labels

Wenn erforderlich, können wir das Vorhandensein von doppelten Labels verhindern, indem wir die Methode `set_flags(allows_duplicate_labels=False)` verwenden.

```python
# Disallowing duplicate labels in a Series
try:
    pd.Series([0, 1, 2], index=["a", "b", "b"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)

# Disallowing duplicate labels in a DataFrame
try:
    pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=["A", "B", "C"]).set_flags(allows_duplicate_labels=False)
except Exception as e:
    print(e)
```
