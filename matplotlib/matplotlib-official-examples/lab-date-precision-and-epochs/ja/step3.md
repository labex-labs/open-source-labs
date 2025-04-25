# datetime を Matplotlib 日付に変換する

エポックが設定されたので、`mdates.date2num`関数を使用して、`datetime`オブジェクトを Matplotlib 日付に変換することができます。

```python
date1 = datetime.datetime(2000, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
