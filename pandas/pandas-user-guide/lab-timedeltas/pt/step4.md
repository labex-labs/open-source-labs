# Realizar Operações

Você pode realizar operações matemáticas em timedeltas.

```python
# Subtract two timedeltas
s = pd.Series(pd.date_range("2012-1-1", periods=3, freq="D"))
s - s.max()
```
