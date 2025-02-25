# Выполнять операции с индексом временного интервала

Вы можете выполнять операции с индексом временного интервала.

```python
# Add a timedelta index to a datetime index
tdi = pd.TimedeltaIndex(["1 days", pd.NaT, "2 days"])
dti = pd.date_range("20130101", periods=3)
(dti + tdi).to_list()
```
