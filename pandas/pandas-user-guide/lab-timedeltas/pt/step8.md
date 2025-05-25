# Usar o Índice Timedelta

Você pode usar o índice timedelta como o índice de objetos pandas.

```python
# Use the timedelta index as the index of a pandas series
s = pd.Series(np.arange(100), index=pd.timedelta_range("1 days", periods=100, freq="h"))
```
