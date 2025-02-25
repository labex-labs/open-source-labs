# Effectuer des opérations

Vous pouvez effectuer des opérations mathématiques sur les écarts temporels.

```python
# Subtract two timedeltas
s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
s - s.max()
```
