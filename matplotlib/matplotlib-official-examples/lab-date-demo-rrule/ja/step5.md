# 日付を設定して乱数データを生成する

開始日と終了日、および各日付間の差分を表すdeltaを設定する必要があります。また、この例のために乱数データを生成する必要もあります。

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```