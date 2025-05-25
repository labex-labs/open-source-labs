# Timedelta Index 로 연산 수행하기

Timedelta index 를 사용하여 연산을 수행할 수 있습니다.

```python
# Add a timedelta index to a datetime index
tdi = pd.TimedeltaIndex(["1 days", pd.NaT, "2 days"])
dti = pd.date_range("20130101", periods=3)
(dti + tdi).to_list()
```
