# Das Überprüfen und Setzen der Flagge für doppelten Labels

Schließlich können wir die Flagge `allows_duplicate_labels` für ein DataFrame überprüfen und setzen.

```python
# Creating a DataFrame and setting allows_duplicate_labels to False
df = pd.DataFrame({"A": [0, 1, 2, 3]}, index=["x", "y", "X", "Y"]).set_flags(allows_duplicate_labels=False)

# Checking the allows_duplicate_labels flag
print(df.flags.allows_duplicate_labels)

# Setting allows_duplicate_labels to True
df2 = df.set_flags(allows_duplicate_labels=True)
print(df2.flags.allows_duplicate_labels)
```
