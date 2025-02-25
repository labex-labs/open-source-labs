# Utiliser l'index d'écart temporel

Vous pouvez utiliser l'index d'écart temporel comme index d'objets pandas.

```python
# Use the timedelta index as the index of a pandas series
s = pd.Series(np.arange(100), index=pd.timedelta_range("1 days", periods=100, freq="h"))
```
