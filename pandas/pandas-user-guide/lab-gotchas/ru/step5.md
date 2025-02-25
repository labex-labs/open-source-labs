# Понимание различий с NumPy

В Pandas и NumPy есть небольшие различия в том, как они вычисляют дисперсию. Это важно учитывать при переходе между двумя библиотеками.

```python
# Variance in pandas
var_pandas = df.var()

# Variance in NumPy
var_numpy = np.var(df.values)
```
