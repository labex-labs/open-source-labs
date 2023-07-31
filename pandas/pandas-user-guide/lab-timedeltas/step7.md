# Create a Timedelta Index

You can generate an index with time deltas.

```python
# Generate a timedelta index
pd.TimedeltaIndex(["1 days", "1 days, 00:00:05", np.timedelta64(2, "D"), datetime.timedelta(days=2, seconds=2)])
```
