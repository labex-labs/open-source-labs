# Usar el índice de timedelta

Puedes usar el índice de timedelta como el índice de objetos de pandas.

```python
# Use the timedelta index as the index of a pandas series
s = pd.Series(np.arange(100), index=pd.timedelta_range("1 days", periods=100, freq="h"))
```
