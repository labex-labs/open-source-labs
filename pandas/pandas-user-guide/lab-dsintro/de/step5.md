# Datenalignment und Arithmetik

Datenalignment ist ein wichtiges Merkmal von pandas. Wenn Sie Operationen auf zwei Objekten ausführen, ordnet pandas sie anhand ihrer zugeordneten Labels an.

```python
# Create two DataFrames
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# Perform addition operation
result = df1 + df2
```
