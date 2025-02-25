# 時間差分インデックスを使った演算を行う

時間差分インデックスを使って演算を行うことができます。

```python
# Add a timedelta index to a datetime index
tdi = pd.TimedeltaIndex(["1 days", pd.NaT, "2 days"])
dti = pd.date_range("20130101", periods=3)
(dti + tdi).to_list()
```
