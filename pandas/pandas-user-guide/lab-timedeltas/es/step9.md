# Realizar operaciones con el índice de timedelta

Puedes realizar operaciones con el índice de timedelta.

```python
# Add a timedelta index to a datetime index
tdi = pd.TimedeltaIndex(["1 days", pd.NaT, "2 days"])
dti = pd.date_range("20130101", periods=3)
(dti + tdi).to_list()
```
