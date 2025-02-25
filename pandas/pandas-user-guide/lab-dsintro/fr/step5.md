# Alignement des données et opérations arithmétiques

L'alignement des données est une fonctionnalité importante de pandas. Lorsque vous effectuez des opérations sur deux objets, pandas les aligne selon leurs étiquettes associées.

```python
# Create two DataFrames
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

# Perform addition operation
result = df1 + df2
```
