# Criar um Índice Timedelta

Você pode gerar um índice com deltas de tempo.

```python
# Generate a timedelta index
pd.TimedeltaIndex(["1 days", "1 days, 00:00:05", np.timedelta64(2, "D"), datetime.timedelta(days=2, seconds=2)])
```
