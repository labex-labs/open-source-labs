# Datenoperationen

Wir können Operationen auf Dataframes durchführen, wie z.B. Sortieren, Anwenden von Funktionen usw.

```python
# Sorting by an axis
df.sort_index(axis=1, ascending=False)

# Applying a function to the data
df.apply(np.cumsum)
```
