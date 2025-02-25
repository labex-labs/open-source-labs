# Comprendre les différences avec NumPy

Pandas et NumPy présentent des différences légères dans la manière dont ils calculent la variance. Il est important de prendre cela en compte lors du passage d'une bibliothèque à l'autre.

```python
# Variance dans pandas
var_pandas = df.var()

# Variance dans NumPy
var_numpy = np.var(df.values)
```
