# 日付を設定し、ランダムなデータを生成する

開始日と終了日、および各日付間の差を表す `delta` を設定する必要があります。また、この例で使用するランダムなデータも生成する必要があります。

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
